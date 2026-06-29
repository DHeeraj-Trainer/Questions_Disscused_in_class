import React, { useState, useEffect, useLayoutEffect, useRef, useMemo, useCallback } from "react";

/* ============================================================================
   codeviz — full platform
   Landing → Library browser (categories → problems) → Studio (writeup + live
   in-browser Python tracer + multi-structure visualizer).
   Tracer below is the project's tracer.py, executed in-browser via Pyodide.
   ========================================================================== */

const TRACER_PY = "\"\"\"\ncodeviz tracer \u2014 captures step-by-step execution of Python code.\n\nDesign notes for the multi-language story (see ARCHITECTURE.md):\n  This is the *reference implementation* of the Trace Protocol. Every language\n  adapter (a JS tracer via node --inspect, a C/C++ tracer via gdb/MI, a JVM\n  agent, etc.) must emit the SAME json schema defined in trace_schema.py.\n  The frontend never knows which language produced a trace.\n\"\"\"\n\nimport sys\nimport json\nimport copy\nimport traceback\nfrom typing import Any, Dict, List, Optional\n\n\n# ---- value snapshotting -----------------------------------------------------\n\nPRIMITIVES = (int, float, str, bool, type(None))\nMAX_DEPTH = 6\nMAX_ITEMS = 200\n\n\ndef classify(value: Any) -> str:\n    \"\"\"Best-effort data-structure tag. Drives which frontend renderer is used.\"\"\"\n    if isinstance(value, bool):\n        return \"bool\"\n    if isinstance(value, (int, float)):\n        return \"number\"\n    if isinstance(value, str):\n        return \"string\"\n    if value is None:\n        return \"null\"\n    if isinstance(value, list):\n        return \"array\"\n    if isinstance(value, tuple):\n        return \"tuple\"\n    if isinstance(value, dict):\n        return \"map\"\n    if isinstance(value, set):\n        return \"set\"\n    # heuristic structural detection for custom classes\n    cls = type(value).__name__.lower()\n    if any(k in cls for k in (\"node\", \"listnode\")):\n        return \"linkedlist_node\"\n    if any(k in cls for k in (\"tree\", \"treenode\")):\n        return \"tree_node\"\n    if any(k in cls for k in (\"stack\",)):\n        return \"stack\"\n    if any(k in cls for k in (\"queue\",)):\n        return \"queue\"\n    if any(k in cls for k in (\"graph\",)):\n        return \"graph\"\n    return \"object\"\n\n\ndef snapshot(value: Any, depth: int = 0, seen: Optional[set] = None) -> Dict[str, Any]:\n    \"\"\"Produce a JSON-safe, depth-limited snapshot of a value with a type tag.\"\"\"\n    if seen is None:\n        seen = set()\n    tag = classify(value)\n\n    if isinstance(value, PRIMITIVES):\n        return {\"type\": tag, \"value\": value}\n\n    oid = id(value)\n    if oid in seen or depth > MAX_DEPTH:\n        return {\"type\": tag, \"ref\": oid, \"truncated\": True}\n    seen = seen | {oid}\n\n    if isinstance(value, (list, tuple)):\n        items = [snapshot(v, depth + 1, seen) for v in value[:MAX_ITEMS]]\n        return {\"type\": tag, \"id\": oid, \"items\": items, \"length\": len(value)}\n\n    if isinstance(value, dict):\n        entries = []\n        for i, (k, v) in enumerate(value.items()):\n            if i >= MAX_ITEMS:\n                break\n            entries.append({\"key\": str(k), \"value\": snapshot(v, depth + 1, seen)})\n        return {\"type\": tag, \"id\": oid, \"entries\": entries, \"length\": len(value)}\n\n    if isinstance(value, set):\n        items = [snapshot(v, depth + 1, seen) for v in list(value)[:MAX_ITEMS]]\n        return {\"type\": tag, \"id\": oid, \"items\": items, \"length\": len(value)}\n\n    # custom object: walk its __dict__\n    fields = {}\n    d = getattr(value, \"__dict__\", {})\n    for i, (k, v) in enumerate(d.items()):\n        if i >= MAX_ITEMS:\n            break\n        fields[k] = snapshot(v, depth + 1, seen)\n    return {\n        \"type\": tag,\n        \"id\": oid,\n        \"class\": type(value).__name__,\n        \"fields\": fields,\n    }\n\n\n# ---- the tracer ------------------------------------------------------------\n\nclass Tracer:\n    def __init__(self, source: str, max_steps: int = 5000):\n        self.source = source\n        self.source_lines = source.splitlines()\n        self.max_steps = max_steps\n        self.steps: List[Dict[str, Any]] = []\n        self.call_depth = 0\n        self._prev_locals: Dict[int, Dict[str, Any]] = {}\n        self._stopped = False\n        self._error: Optional[Dict[str, Any]] = None\n\n    def _record(self, frame, event: str, note: str = \"\"):\n        if len(self.steps) >= self.max_steps:\n            self._stopped = True\n            return\n        lineno = frame.f_lineno\n        func = frame.f_code.co_name\n        # only capture user code (the exec'd module), skip our own frames\n        if frame.f_code.co_filename != \"<user_code>\":\n            return\n\n        locals_snap = {}\n        changed = []\n        prev = self._prev_locals.get(id(frame), {})\n        for name, val in frame.f_locals.items():\n            if name.startswith(\"__\"):\n                continue\n            snap = snapshot(val)\n            locals_snap[name] = snap\n            # detect change vs previous step in this frame\n            if name not in prev or prev[name] != snap:\n                changed.append(name)\n        self._prev_locals[id(frame)] = {k: v for k, v in locals_snap.items()}\n\n        self.steps.append({\n            \"step\": len(self.steps),\n            \"event\": event,\n            \"line\": lineno,\n            \"code\": self.source_lines[lineno - 1] if 0 < lineno <= len(self.source_lines) else \"\",\n            \"function\": func,\n            \"depth\": self.call_depth,\n            \"locals\": locals_snap,\n            \"changed\": changed,\n            \"note\": note,\n        })\n\n    def _trace(self, frame, event, arg):\n        if self._stopped:\n            return None\n        if event == \"call\":\n            self.call_depth += 1\n            self._record(frame, \"call\", f\"\u2192 enter {frame.f_code.co_name}()\")\n        elif event == \"line\":\n            self._record(frame, \"line\")\n        elif event == \"return\":\n            self._record(frame, \"return\", f\"\u2190 {frame.f_code.co_name}() returns {arg!r}\")\n            self.call_depth = max(0, self.call_depth - 1)\n        elif event == \"exception\":\n            exc_type, exc_val, _ = arg\n            self._record(frame, \"exception\", f\"\u26a0 {exc_type.__name__}: {exc_val}\")\n        return self._trace\n\n    def run(self) -> Dict[str, Any]:\n        code = compile(self.source, \"<user_code>\", \"exec\")\n        sandbox: Dict[str, Any] = {\"__name__\": \"__main__\"}\n        sys.settrace(self._trace)\n        try:\n            exec(code, sandbox)\n        except Exception as e:\n            self._error = {\n                \"type\": type(e).__name__,\n                \"message\": str(e),\n                \"traceback\": traceback.format_exc(),\n            }\n        finally:\n            sys.settrace(None)\n\n        return {\n            \"language\": \"python\",\n            \"source\": self.source,\n            \"steps\": self.steps,\n            \"stepCount\": len(self.steps),\n            \"truncated\": self._stopped,\n            \"error\": self._error,\n        }\n\n\ndef trace_source(source: str, max_steps: int = 5000) -> Dict[str, Any]:\n    return Tracer(source, max_steps=max_steps).run()\n";
const JS_TRACER_SRC = "/* jsTracer \u2014 produces the SAME trace schema as tracer.py, for JavaScript.\n   Strategy: parse with acorn, inject __step__(line, snapshotFn) before each\n   statement inside function bodies and the top level, then execute with a\n   trapping runtime that records steps. Variable state is captured by passing\n   a live `() => ({...localBindings})` thunk \u2014 but since JS has no settrace,\n   we instrument explicit `__capture__` calls after declarations/assignments.\n\n   This file is written to be embedded as a string and run in the browser,\n   where `acorn` and `astring` are loaded from CDN as globals.\n*/\n\nfunction buildJsTracer(acorn, astring) {\n  const MAX_STEPS = 5000, MAX_ITEMS = 200, MAX_DEPTH = 6;\n\n  function classify(v) {\n    if (v === null || v === undefined) return \"null\";\n    if (typeof v === \"boolean\") return \"bool\";\n    if (typeof v === \"number\") return \"number\";\n    if (typeof v === \"string\") return \"string\";\n    if (Array.isArray(v)) return \"array\";\n    if (v instanceof Map) return \"map\";\n    if (v instanceof Set) return \"set\";\n    const cn = (v.constructor && v.constructor.name || \"\").toLowerCase();\n    if (cn.includes(\"node\") || cn.includes(\"listnode\")) return \"linkedlist_node\";\n    if (cn.includes(\"tree\")) return \"tree_node\";\n    return \"object\";\n  }\n\n  function snapshot(v, depth, seen) {\n    const tag = classify(v);\n    if (tag === \"number\" || tag === \"string\" || tag === \"bool\")\n      return { type: tag, value: v };\n    if (tag === \"null\") return { type: \"null\", value: null };\n    if (depth > MAX_DEPTH) return { type: tag, truncated: true };\n    if (seen.has(v)) return { type: tag, truncated: true };\n    seen.add(v);\n    if (tag === \"array\" || tag === \"set\") {\n      const arr = tag === \"set\" ? Array.from(v) : v;\n      return { type: tag, items: arr.slice(0, MAX_ITEMS).map((x) => snapshot(x, depth + 1, seen)), length: arr.length };\n    }\n    if (tag === \"map\") {\n      const entries = [];\n      let i = 0;\n      for (const [k, val] of v) { if (i++ >= MAX_ITEMS) break; entries.push({ key: String(k), value: snapshot(val, depth + 1, seen) }); }\n      return { type: \"map\", entries, length: v.size };\n    }\n    // plain object / class instance\n    const fields = {};\n    let i = 0;\n    for (const k of Object.keys(v)) { if (i++ >= MAX_ITEMS) break; fields[k] = snapshot(v[k], depth + 1, seen); }\n    return { type: tag, class: v.constructor ? v.constructor.name : \"Object\", fields };\n  }\n\n  function snap(v) { return snapshot(v, 0, new Set()); }\n\n  // ---- instrumentation ----\n  function instrument(code) {\n    const ast = acorn.parse(code, { ecmaVersion: 2022, locations: true });\n\n    function wrapBody(body, fnName) {\n      const out = [];\n      for (const stmt of body) {\n        const line = stmt.loc.start.line;\n        // a probe statement: __step__(line, fnName, () => collectVars())\n        out.push({\n          type: \"ExpressionStatement\",\n          expression: {\n            type: \"CallExpression\",\n            callee: { type: \"Identifier\", name: \"__step__\" },\n            arguments: [\n              { type: \"Literal\", value: line },\n              { type: \"Literal\", value: fnName },\n              // thunk returning the in-scope variables we can see:\n              {\n                type: \"ArrowFunctionExpression\", params: [], expression: true,\n                body: scopeCollector(),\n              },\n            ],\n          },\n        });\n        out.push(stmt);\n      }\n      return out;\n    }\n\n    // builds `(typeof a!=='undefined'?{a}:{}) ...` is hard generically;\n    // instead we capture via a runtime trick: eval-free, we rely on the\n    // function-level `__locals__()` injected at the top of each scope.\n    function scopeCollector() {\n      // returns AST for: __locals__()\n      return { type: \"CallExpression\", callee: { type: \"Identifier\", name: \"__locals__\" }, arguments: [] };\n    }\n\n    // We need __locals__ to see real bindings. Simplest reliable method:\n    // inject `const __locals__ = () => ({ ...binding names ... })` is also hard.\n    // Pragmatic approach: capture declared names per scope by static analysis,\n    // then build an object expression referencing them, guarded by typeof.\n    // To keep this robust we instead transform: at each step, collect the set\n    // of identifiers declared so far in the function and read them.\n\n    // Re-walk: collect declared identifiers per function scope.\n    return ast;\n  }\n\n  // The static-analysis instrumentation above is fiddly; use the proven approach:\n  // transform the code so every variable declaration ALSO assigns into a\n  // per-frame __scope__ object, and probes read __scope__.\n  function instrument2(code) {\n    const ast = acorn.parse(code, { ecmaVersion: 2022, locations: true });\n\n    function transformBlock(body) {\n      const out = [];\n      for (const stmt of body) {\n        const line = stmt.loc.start.line;\n        out.push(probe(line));\n        // capture declarations into __scope__\n        if (stmt.type === \"VariableDeclaration\") {\n          out.push(stmt);\n          for (const d of stmt.declarations) {\n            if (d.id.type === \"Identifier\") out.push(assignScope(d.id.name));\n          }\n        } else if (stmt.type === \"ExpressionStatement\" &&\n                   stmt.expression.type === \"AssignmentExpression\" &&\n                   stmt.expression.left.type === \"Identifier\") {\n          out.push(stmt);\n          out.push(assignScope(stmt.expression.left.name));\n        } else if (stmt.type === \"ForStatement\" || stmt.type === \"WhileStatement\") {\n          // record the for-init variable(s) so loop counters are visible\n          const preRecords = [];\n          if (stmt.type === \"ForStatement\" && stmt.init && stmt.init.type === \"VariableDeclaration\") {\n            for (const d of stmt.init.declarations) if (d.id.type === \"Identifier\") preRecords.push(d.id.name);\n          }\n          if (stmt.body && stmt.body.type === \"BlockStatement\") {\n            // at the top of each iteration: re-record loop vars + probe, then body\n            const loopHead = [];\n            for (const nm of preRecords) loopHead.push(assignScope(nm));\n            loopHead.push(probe(stmt.loc.start.line));\n            stmt.body.body = loopHead.concat(transformBlock(stmt.body.body));\n          }\n          out.push(stmt);\n        } else if (stmt.type === \"IfStatement\") {\n          if (stmt.consequent.type === \"BlockStatement\") stmt.consequent.body = transformBlock(stmt.consequent.body);\n          if (stmt.alternate && stmt.alternate.type === \"BlockStatement\") stmt.alternate.body = transformBlock(stmt.alternate.body);\n          out.push(stmt);\n        } else if (stmt.type === \"FunctionDeclaration\") {\n          // record params into scope at the top of the body, then transform body\n          const paramRecords = stmt.params\n            .filter((p) => p.type === \"Identifier\")\n            .map((p) => assignScope(p.name));\n          stmt.body.body = paramRecords.concat(transformBlock(stmt.body.body));\n          out.push(stmt);\n        } else {\n          out.push(stmt);\n        }\n      }\n      return out;\n    }\n    function probe(line) {\n      return { type: \"ExpressionStatement\", expression: { type: \"CallExpression\",\n        callee: { type: \"Identifier\", name: \"__step__\" },\n        arguments: [{ type: \"Literal\", value: line }] } };\n    }\n    function assignScope(name) {\n      // __record__(\"name\", name)\n      return { type: \"ExpressionStatement\", expression: { type: \"CallExpression\",\n        callee: { type: \"Identifier\", name: \"__record__\" },\n        arguments: [{ type: \"Literal\", value: name }, { type: \"Identifier\", name }] } };\n    }\n    ast.body = transformBlock(ast.body);\n    return astring.generate(ast);\n  }\n\n  function run(code) {\n    const steps = [];\n    let scope = {};\n    let curLine = 0;\n    let error = null;\n    let stopped = false;\n\n    const __record__ = (name, val) => { scope[name] = val; };\n    const __step__ = (line) => {\n      if (steps.length >= MAX_STEPS) { stopped = true; throw new Error(\"__MAXSTEPS__\"); }\n      curLine = line;\n      const locals = {};\n      const changed = [];\n      const prev = steps.length ? steps[steps.length - 1]._raw : {};\n      for (const k of Object.keys(scope)) {\n        const s = snap(scope[k]);\n        locals[k] = s;\n        if (JSON.stringify(prev[k]) !== JSON.stringify(s)) changed.push(k);\n      }\n      steps.push({\n        step: steps.length, event: \"line\", line, code: \"\",\n        function: \"main\", depth: 0, locals, changed, note: \"\",\n        _raw: locals,\n      });\n    };\n\n    let instrumented;\n    try { instrumented = instrument2(code); }\n    catch (e) { return { language: \"javascript\", source: code, steps: [], stepCount: 0, error: { type: \"SyntaxError\", message: String(e.message || e) } }; }\n\n    try {\n      const fn = new Function(\"__step__\", \"__record__\", instrumented);\n      fn(__step__, __record__);\n    } catch (e) {\n      if (e.message !== \"__MAXSTEPS__\") error = { type: e.name || \"Error\", message: String(e.message || e) };\n    }\n\n    // attach source lines + strip _raw\n    const lines = code.split(\"\\n\");\n    for (const s of steps) { s.code = lines[s.line - 1] || \"\"; delete s._raw; }\n    return { language: \"javascript\", source: code, steps, stepCount: steps.length, truncated: stopped, error };\n  }\n\n  return { run, instrument2, snap };\n}";
const LIBRARY = [{"category": "Arrays", "title": "Bubble Sort", "difficulty": "Easy", "statement": "Sort an array in ascending order by repeatedly swapping adjacent out-of-order elements. Watch the largest values 'bubble' to the end on each pass.", "hints": ["The largest unsorted element reaches its final spot after each outer pass.", "The inner loop can shrink each pass \u2014 the tail is already sorted."], "complexity": "Time O(n\u00b2) \u00b7 Space O(1)", "mistakes": ["Looping the inner range to n instead of n-1-i (redundant comparisons).", "Forgetting the swap is simultaneous: a[j], a[j+1] = a[j+1], a[j]."], "code": "def bubble(a):\n    n = len(a)\n    for i in range(n):\n        for j in range(n - 1 - i):\n            if a[j] > a[j + 1]:\n                a[j], a[j + 1] = a[j + 1], a[j]\n    return a\n\nbubble([5, 2, 4, 1, 3])\n"}, {"category": "Arrays", "title": "Two Sum (sorted, two pointers)", "difficulty": "Easy", "statement": "Given a sorted array and a target, find two values that sum to the target using a left/right pointer pair converging inward.", "hints": ["If the current sum is too small, move the left pointer right.", "If too large, move the right pointer left."], "complexity": "Time O(n) \u00b7 Space O(1)", "mistakes": ["Using this on an unsorted array \u2014 two pointers require sorted input.", "Moving the wrong pointer when sum overshoots."], "code": "def two_sum(a, target):\n    lo, hi = 0, len(a) - 1\n    while lo < hi:\n        s = a[lo] + a[hi]\n        if s == target:\n            return [lo, hi]\n        if s < target:\n            lo += 1\n        else:\n            hi -= 1\n    return [-1, -1]\n\ntwo_sum([1, 3, 4, 6, 8, 11], 10)\n"}, {"category": "Arrays", "title": "Kadane \u2014 Max Subarray", "difficulty": "Medium", "statement": "Find the largest sum of any contiguous subarray. Track a running best-ending-here and the global best.", "hints": ["At each index, either extend the previous subarray or start fresh.", "cur = max(x, cur + x)."], "complexity": "Time O(n) \u00b7 Space O(1)", "mistakes": ["Initializing best to 0 \u2014 fails on all-negative arrays.", "Resetting cur to 0 instead of to the current element."], "code": "def max_subarray(a):\n    best = a[0]\n    cur = a[0]\n    for x in a[1:]:\n        cur = max(x, cur + x)\n        best = max(best, cur)\n    return best\n\nmax_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])\n"}, {"category": "Arrays", "title": "Binary Search", "difficulty": "Easy", "statement": "Find a target's index in a sorted array by repeatedly halving the search range.", "hints": ["Compute mid as lo + (hi - lo) // 2 to avoid overflow in other languages.", "Narrow to the half that could contain the target."], "complexity": "Time O(log n) \u00b7 Space O(1)", "mistakes": ["Off-by-one in the loop condition (lo <= hi vs lo < hi).", "Updating lo/hi to mid instead of mid\u00b11, causing infinite loops."], "code": "def binary_search(a, target):\n    lo, hi = 0, len(a) - 1\n    while lo <= hi:\n        mid = lo + (hi - lo) // 2\n        if a[mid] == target:\n            return mid\n        if a[mid] < target:\n            lo = mid + 1\n        else:\n            hi = mid - 1\n    return -1\n\nbinary_search([1, 3, 5, 7, 9, 11, 13], 9)\n"}, {"category": "Stacks & Queues", "title": "Queue via Two Stacks", "difficulty": "Medium", "statement": "Implement a FIFO queue using two LIFO stacks. Elements are transferred between stacks to reverse order on demand.", "hints": ["Only refill out_stack when it is empty.", "Transferring all of in_stack reverses insertion order \u2014 restoring FIFO."], "complexity": "enqueue O(1) \u00b7 dequeue amortized O(1)", "mistakes": ["Transferring on every dequeue instead of only when out_stack is empty.", "Transferring out_stack back into in_stack unnecessarily."], "code": "class QueueViaStacks:\n    def __init__(self):\n        self.in_stack = []\n        self.out_stack = []\n    def enqueue(self, x):\n        self.in_stack.append(x)\n    def dequeue(self):\n        if not self.out_stack:\n            while self.in_stack:\n                self.out_stack.append(self.in_stack.pop())\n        return self.out_stack.pop()\n\nq = QueueViaStacks()\nq.enqueue(1); q.enqueue(2); q.enqueue(3)\na = q.dequeue()\nq.enqueue(4)\nb = q.dequeue()\n"}, {"category": "Stacks & Queues", "title": "Valid Parentheses", "difficulty": "Easy", "statement": "Check whether a string of brackets is balanced. Push openers; on a closer, the top must be its match.", "hints": ["Map each closer to its opener.", "An empty stack at the end means perfectly balanced."], "complexity": "Time O(n) \u00b7 Space O(n)", "mistakes": ["Forgetting to check the stack is non-empty before popping.", "Not verifying the stack is empty at the end."], "code": "def is_valid(s):\n    stack = []\n    pairs = {')': '(', ']': '[', '}': '{'}\n    for ch in s:\n        if ch in '([{':\n            stack.append(ch)\n        else:\n            if not stack or stack.pop() != pairs[ch]:\n                return False\n    return len(stack) == 0\n\nis_valid(\"([]{})\")\n"}, {"category": "Stacks & Queues", "title": "Next Greater Element", "difficulty": "Medium", "statement": "For each element, find the next element to its right that is larger, using a monotonic decreasing stack of indices.", "hints": ["Keep a stack of indices whose answer is still unknown.", "When a bigger value appears, it resolves everything smaller on the stack."], "complexity": "Time O(n) \u00b7 Space O(n)", "mistakes": ["Storing values instead of indices, losing where to write the answer.", "Using a non-monotonic stack and re-scanning (O(n\u00b2))."], "code": "def next_greater(a):\n    res = [-1] * len(a)\n    stack = []\n    for i, x in enumerate(a):\n        while stack and a[stack[-1]] < x:\n            res[stack.pop()] = x\n        stack.append(i)\n    return res\n\nnext_greater([2, 1, 4, 3, 5])\n"}, {"category": "Linked Lists", "title": "Reverse a Linked List", "difficulty": "Easy", "statement": "Reverse a singly linked list in place by rewiring each node's next pointer to its predecessor.", "hints": ["Save next before overwriting it.", "Three pointers march together: prev, head, nxt."], "complexity": "Time O(n) \u00b7 Space O(1)", "mistakes": ["Overwriting head.next before saving it \u2014 loses the rest of the list.", "Returning head (now null) instead of prev."], "code": "class Node:\n    def __init__(self, val):\n        self.val = val\n        self.next = None\n\ndef build(vals):\n    head = None\n    for v in reversed(vals):\n        n = Node(v)\n        n.next = head\n        head = n\n    return head\n\ndef reverse(head):\n    prev = None\n    while head:\n        nxt = head.next\n        head.next = prev\n        prev = head\n        head = nxt\n    return prev\n\nreverse(build([1, 2, 3, 4]))\n"}, {"category": "Linked Lists", "title": "Cycle Detection (Floyd)", "difficulty": "Medium", "statement": "Detect whether a linked list contains a cycle using slow and fast pointers that meet if a loop exists.", "hints": ["Fast moves two steps, slow moves one.", "If they ever meet, there is a cycle; if fast hits null, there isn't."], "complexity": "Time O(n) \u00b7 Space O(1)", "mistakes": ["Not null-checking fast and fast.next before advancing.", "Comparing values instead of node identity."], "code": "class Node:\n    def __init__(self, val):\n        self.val = val\n        self.next = None\n\ndef build_no_cycle(vals):\n    head = None\n    for v in reversed(vals):\n        n = Node(v)\n        n.next = head\n        head = n\n    return head\n\ndef has_cycle(head):\n    slow = head\n    fast = head\n    while fast and fast.next:\n        slow = slow.next\n        fast = fast.next.next\n        if slow is fast:\n            return True\n    return False\n\nhas_cycle(build_no_cycle([1, 2, 3, 4]))\n"}, {"category": "Linked Lists", "title": "Merge Two Sorted Lists", "difficulty": "Easy", "statement": "Merge two sorted linked lists into one sorted list by repeatedly attaching the smaller head.", "hints": ["A dummy head node simplifies edge cases.", "Attach whichever current node is smaller, then advance it."], "complexity": "Time O(n+m) \u00b7 Space O(1)", "mistakes": ["Forgetting to attach the non-empty remainder at the end.", "Losing the merged head without a dummy node."], "code": "class Node:\n    def __init__(self, val):\n        self.val = val\n        self.next = None\n\ndef build(vals):\n    head = None\n    for v in reversed(vals):\n        n = Node(v)\n        n.next = head\n        head = n\n    return head\n\ndef merge(a, b):\n    dummy = Node(0)\n    tail = dummy\n    while a and b:\n        if a.val <= b.val:\n            tail.next = a\n            a = a.next\n        else:\n            tail.next = b\n            b = b.next\n        tail = tail.next\n    tail.next = a if a else b\n    return dummy.next\n\nmerge(build([1, 3, 5]), build([2, 4, 6]))\n"}, {"category": "Trees", "title": "BST Insert", "difficulty": "Easy", "statement": "Insert values into a binary search tree. Each value walks left (smaller) or right (larger) until it finds an empty slot.", "hints": ["Recursion mirrors the structure: insert into the correct subtree.", "A None root is where the new node belongs."], "complexity": "Time O(h) per insert (h = height) \u00b7 Space O(h)", "mistakes": ["Not reassigning root.left/right to the recursive result.", "Allowing duplicates inconsistently (left vs right)."], "code": "class TreeNode:\n    def __init__(self, val):\n        self.val = val\n        self.left = None\n        self.right = None\n\ndef insert(root, val):\n    if root is None:\n        return TreeNode(val)\n    if val < root.val:\n        root.left = insert(root.left, val)\n    else:\n        root.right = insert(root.right, val)\n    return root\n\nroot = None\nfor v in [5, 3, 8, 1, 4, 7]:\n    root = insert(root, v)\n"}, {"category": "Trees", "title": "Inorder Traversal", "difficulty": "Easy", "statement": "Visit a BST's nodes in sorted order: left subtree, then node, then right subtree.", "hints": ["Inorder of a BST yields values in ascending order.", "Recurse left, record, recurse right."], "complexity": "Time O(n) \u00b7 Space O(h)", "mistakes": ["Recording the node before recursing left (gives wrong order).", "Not handling the None base case."], "code": "class TreeNode:\n    def __init__(self, val):\n        self.val = val\n        self.left = None\n        self.right = None\n\ndef insert(root, val):\n    if root is None:\n        return TreeNode(val)\n    if val < root.val:\n        root.left = insert(root.left, val)\n    else:\n        root.right = insert(root.right, val)\n    return root\n\ndef inorder(root, out):\n    if root is None:\n        return\n    inorder(root.left, out)\n    out.append(root.val)\n    inorder(root.right, out)\n    return out\n\nroot = None\nfor v in [5, 3, 8, 1, 4]:\n    root = insert(root, v)\nresult = []\ninorder(root, result)\n"}, {"category": "Trees", "title": "Max Depth", "difficulty": "Easy", "statement": "Compute the height of a binary tree: the longest root-to-leaf path measured in nodes.", "hints": ["Depth of a node is 1 + max(depth(left), depth(right)).", "An empty tree has depth 0."], "complexity": "Time O(n) \u00b7 Space O(h)", "mistakes": ["Returning max of children without adding 1 for the current node.", "Off-by-one between counting nodes vs edges."], "code": "class TreeNode:\n    def __init__(self, val):\n        self.val = val\n        self.left = None\n        self.right = None\n\ndef insert(root, val):\n    if root is None:\n        return TreeNode(val)\n    if val < root.val:\n        root.left = insert(root.left, val)\n    else:\n        root.right = insert(root.right, val)\n    return root\n\ndef max_depth(root):\n    if root is None:\n        return 0\n    return 1 + max(max_depth(root.left), max_depth(root.right))\n\nroot = None\nfor v in [5, 3, 8, 1]:\n    root = insert(root, v)\nmax_depth(root)\n"}, {"category": "Graphs", "title": "Breadth-First Search", "difficulty": "Medium", "statement": "Explore a graph level by level from a start node using a queue, marking nodes visited as they are discovered.", "hints": ["A queue gives the level-by-level (FIFO) order.", "Mark a node visited when you enqueue it, not when you dequeue it."], "complexity": "Time O(V + E) \u00b7 Space O(V)", "mistakes": ["Marking visited on dequeue, allowing duplicates in the queue.", "Using a list as a queue and popping from the front (O(n))."], "code": "from collections import deque\n\ndef bfs(graph, start):\n    visited = [start]\n    q = deque([start])\n    while q:\n        node = q.popleft()\n        for nb in graph[node]:\n            if nb not in visited:\n                visited.append(nb)\n                q.append(nb)\n    return visited\n\ng = {0: [1, 2], 1: [3], 2: [3], 3: []}\nbfs(g, 0)\n"}, {"category": "Graphs", "title": "Depth-First Search", "difficulty": "Medium", "statement": "Explore a graph by going as deep as possible before backtracking, using recursion and a visited set.", "hints": ["Recursion uses the call stack as your traversal stack.", "Mark visited on entry to avoid revisiting."], "complexity": "Time O(V + E) \u00b7 Space O(V)", "mistakes": ["Not marking visited, causing infinite loops on cycles.", "Mutating the visited structure inconsistently across calls."], "code": "def dfs(graph, node, visited):\n    visited.append(node)\n    for nb in graph[node]:\n        if nb not in visited:\n            dfs(graph, nb, visited)\n    return visited\n\ng = {0: [1, 2], 1: [3], 2: [3], 3: []}\norder = []\ndfs(g, 0, order)\n"}, {"category": "Graphs", "title": "Count Connected Components", "difficulty": "Medium", "statement": "Count how many separate clusters exist in an undirected graph by running a traversal from each unvisited node.", "hints": ["Each new traversal you must start marks one fresh component.", "Reuse one visited set across all starts."], "complexity": "Time O(V + E) \u00b7 Space O(V)", "mistakes": ["Resetting visited inside the loop, recounting nodes.", "Forgetting undirected edges appear in both adjacency lists."], "code": "def dfs(graph, node, visited):\n    visited.append(node)\n    for nb in graph[node]:\n        if nb not in visited:\n            dfs(graph, nb, visited)\n\ndef count_components(graph):\n    visited = []\n    count = 0\n    for node in graph:\n        if node not in visited:\n            count += 1\n            dfs(graph, node, visited)\n    return count\n\ng = {0: [1], 1: [0], 2: [3], 3: [2], 4: []}\ncount_components(g)\n"}, {"category": "Arrays", "title": "Move Zeroes", "difficulty": "Easy", "statement": "Move all zeroes to the end of the array while keeping the relative order of non-zero elements, in place.", "hints": ["Keep a write pointer for the next non-zero slot.", "Swap or overwrite as you scan with a read pointer."], "complexity": "Time O(n) \u00b7 Space O(1)", "mistakes": ["Breaking the relative order of non-zero elements.", "Using extra arrays when in-place is required."], "code": "def move_zeroes(a):\n    w = 0\n    for r in range(len(a)):\n        if a[r] != 0:\n            a[w], a[r] = a[r], a[w]\n            w += 1\n    return a\n\nmove_zeroes([0, 1, 0, 3, 12])\n"}, {"category": "Arrays", "title": "Dutch National Flag", "difficulty": "Medium", "statement": "Sort an array of 0s, 1s, and 2s in a single pass using three pointers (low, mid, high).", "hints": ["mid scans; low marks the 0-region edge, high the 2-region edge.", "On a 2, swap with high and DON'T advance mid yet."], "complexity": "Time O(n) \u00b7 Space O(1)", "mistakes": ["Advancing mid after swapping with high (skips an unchecked value).", "Using a counting sort when one pass is intended."], "code": "def sort_colors(a):\n    lo, mid, hi = 0, 0, len(a) - 1\n    while mid <= hi:\n        if a[mid] == 0:\n            a[lo], a[mid] = a[mid], a[lo]\n            lo += 1\n            mid += 1\n        elif a[mid] == 1:\n            mid += 1\n        else:\n            a[mid], a[hi] = a[hi], a[mid]\n            hi -= 1\n    return a\n\nsort_colors([2, 0, 2, 1, 1, 0])\n"}, {"category": "Arrays", "title": "Product Except Self", "difficulty": "Medium", "statement": "Return an array where each element is the product of all others, without using division.", "hints": ["First pass: prefix products. Second pass: multiply by suffix products.", "Two sweeps, left-to-right then right-to-left."], "complexity": "Time O(n) \u00b7 Space O(1) extra", "mistakes": ["Reaching for division (disallowed and breaks on zeros).", "Forgetting to seed prefix/suffix accumulators at 1."], "code": "def product_except_self(a):\n    n = len(a)\n    res = [1] * n\n    prefix = 1\n    for i in range(n):\n        res[i] = prefix\n        prefix *= a[i]\n    suffix = 1\n    for i in range(n - 1, -1, -1):\n        res[i] *= suffix\n        suffix *= a[i]\n    return res\n\nproduct_except_self([1, 2, 3, 4])\n"}, {"category": "Dynamic Programming", "title": "Fibonacci (bottom-up)", "difficulty": "Easy", "statement": "Compute the nth Fibonacci number by building a table from the base cases upward.", "hints": ["dp[i] = dp[i-1] + dp[i-2].", "Only the last two values are ever needed."], "complexity": "Time O(n) \u00b7 Space O(n) (or O(1) optimized)", "mistakes": ["Naive recursion recomputes the same subproblems exponentially.", "Off-by-one in the base cases."], "code": "def fib(n):\n    dp = [0] * (n + 1)\n    dp[1] = 1\n    for i in range(2, n + 1):\n        dp[i] = dp[i - 1] + dp[i - 2]\n    return dp[n]\n\nfib(8)\n"}, {"category": "Dynamic Programming", "title": "Climbing Stairs", "difficulty": "Easy", "statement": "Count distinct ways to climb n stairs taking 1 or 2 steps at a time. The DP table mirrors Fibonacci.", "hints": ["ways[i] = ways[i-1] + ways[i-2].", "Reaching step i comes from i-1 (one step) or i-2 (two steps)."], "complexity": "Time O(n) \u00b7 Space O(n)", "mistakes": ["Wrong base cases for steps 0 and 1.", "Treating ordered step sequences as unordered."], "code": "def climb_stairs(n):\n    dp = [0] * (n + 1)\n    dp[0] = 1\n    dp[1] = 1\n    for i in range(2, n + 1):\n        dp[i] = dp[i - 1] + dp[i - 2]\n    return dp[n]\n\nclimb_stairs(5)\n"}, {"category": "Dynamic Programming", "title": "Coin Change (min coins)", "difficulty": "Medium", "statement": "Find the fewest coins that sum to an amount. Build a table of best answers for every sub-amount.", "hints": ["dp[x] = 1 + min(dp[x - coin]) over all coins that fit.", "Initialize dp with infinity except dp[0] = 0."], "complexity": "Time O(amount \u00b7 coins) \u00b7 Space O(amount)", "mistakes": ["Greedy coin picking fails for arbitrary denominations.", "Not guarding against amounts that can't be formed."], "code": "def coin_change(coins, amount):\n    INF = amount + 1\n    dp = [INF] * (amount + 1)\n    dp[0] = 0\n    for x in range(1, amount + 1):\n        for c in coins:\n            if c <= x:\n                dp[x] = min(dp[x], dp[x - c] + 1)\n    return dp[amount] if dp[amount] != INF else -1\n\ncoin_change([1, 2, 5], 11)\n"}, {"category": "Dynamic Programming", "title": "Longest Common Subsequence", "difficulty": "Medium", "statement": "Find the length of the longest subsequence present in both strings, using a 2D DP grid.", "hints": ["If chars match: dp[i][j] = dp[i-1][j-1] + 1.", "Else take the max of dropping one char from either string."], "complexity": "Time O(n\u00b7m) \u00b7 Space O(n\u00b7m)", "mistakes": ["Confusing subsequence (non-contiguous) with substring.", "Indexing the grid off by one against the strings."], "code": "def lcs(a, b):\n    n, m = len(a), len(b)\n    dp = [[0] * (m + 1) for _ in range(n + 1)]\n    for i in range(1, n + 1):\n        for j in range(1, m + 1):\n            if a[i - 1] == b[j - 1]:\n                dp[i][j] = dp[i - 1][j - 1] + 1\n            else:\n                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])\n    return dp[n][m]\n\nlcs(\"ABCBDAB\", \"BDCAB\")\n"}, {"category": "Stacks & Queues", "title": "Min Stack", "difficulty": "Medium", "statement": "Design a stack that also returns its minimum in O(1) by keeping a parallel stack of running minimums.", "hints": ["Push to the min-stack the smaller of the new value and current min.", "Pop both stacks together."], "complexity": "push/pop/min all O(1)", "mistakes": ["Scanning for the min on each query (O(n)).", "Forgetting to pop the min-stack in lockstep."], "code": "class MinStack:\n    def __init__(self):\n        self.stack = []\n        self.mins = []\n    def push(self, x):\n        self.stack.append(x)\n        m = x if not self.mins else min(x, self.mins[-1])\n        self.mins.append(m)\n    def pop(self):\n        self.mins.pop()\n        return self.stack.pop()\n    def get_min(self):\n        return self.mins[-1]\n\ns = MinStack()\ns.push(5); s.push(2); s.push(7); s.push(1)\na = s.get_min()\ns.pop()\nb = s.get_min()\n"}, {"category": "Stacks & Queues", "title": "Daily Temperatures", "difficulty": "Medium", "statement": "For each day, find how many days until a warmer temperature, using a monotonic stack of indices.", "hints": ["Stack holds indices whose answer is pending.", "A warmer day resolves all cooler days on the stack."], "complexity": "Time O(n) \u00b7 Space O(n)", "mistakes": ["Storing temperatures instead of indices.", "Brute-force O(n\u00b2) scanning forward each day."], "code": "def daily_temps(temps):\n    res = [0] * len(temps)\n    stack = []\n    for i, t in enumerate(temps):\n        while stack and temps[stack[-1]] < t:\n            j = stack.pop()\n            res[j] = i - j\n        stack.append(i)\n    return res\n\ndaily_temps([73, 74, 75, 71, 69, 72, 76, 73])\n"}, {"category": "Linked Lists", "title": "Middle of Linked List", "difficulty": "Easy", "statement": "Find the middle node using slow/fast pointers \u2014 fast moves twice as fast, so slow lands in the middle.", "hints": ["When fast reaches the end, slow is at the midpoint.", "For even length, this returns the second middle."], "complexity": "Time O(n) \u00b7 Space O(1)", "mistakes": ["Counting length first then re-walking (two passes).", "Null-check errors on fast and fast.next."], "code": "class Node:\n    def __init__(self, val):\n        self.val = val\n        self.next = None\n\ndef build(vals):\n    head = None\n    for v in reversed(vals):\n        n = Node(v)\n        n.next = head\n        head = n\n    return head\n\ndef middle(head):\n    slow = head\n    fast = head\n    while fast and fast.next:\n        slow = slow.next\n        fast = fast.next.next\n    return slow\n\nmiddle(build([1, 2, 3, 4, 5]))\n"}, {"category": "Linked Lists", "title": "Remove Nth From End", "difficulty": "Medium", "statement": "Remove the nth node from the end in one pass using two pointers spaced n apart.", "hints": ["Advance a lead pointer n steps first.", "Then move both until lead hits the end; trailing sits before the target."], "complexity": "Time O(n) \u00b7 Space O(1)", "mistakes": ["Off-by-one in the gap, removing the wrong node.", "Not using a dummy head for removing the first node."], "code": "class Node:\n    def __init__(self, val):\n        self.val = val\n        self.next = None\n\ndef build(vals):\n    head = None\n    for v in reversed(vals):\n        n = Node(v)\n        n.next = head\n        head = n\n    return head\n\ndef remove_nth(head, n):\n    dummy = Node(0)\n    dummy.next = head\n    lead = dummy\n    trail = dummy\n    for _ in range(n):\n        lead = lead.next\n    while lead.next:\n        lead = lead.next\n        trail = trail.next\n    trail.next = trail.next.next\n    return dummy.next\n\nremove_nth(build([1, 2, 3, 4, 5]), 2)\n"}, {"category": "Trees", "title": "Level Order Traversal", "difficulty": "Medium", "statement": "Visit tree nodes level by level (BFS), collecting each depth's values, using a queue.", "hints": ["Process the queue one full level at a time.", "Track the count of nodes at the current level."], "complexity": "Time O(n) \u00b7 Space O(n)", "mistakes": ["Mixing levels by not snapshotting the level size.", "Using DFS and expecting level grouping."], "code": "from collections import deque\n\nclass TreeNode:\n    def __init__(self, val):\n        self.val = val\n        self.left = None\n        self.right = None\n\ndef insert(root, val):\n    if root is None:\n        return TreeNode(val)\n    if val < root.val:\n        root.left = insert(root.left, val)\n    else:\n        root.right = insert(root.right, val)\n    return root\n\ndef level_order(root):\n    result = []\n    q = deque([root])\n    while q:\n        size = len(q)\n        level = []\n        for _ in range(size):\n            node = q.popleft()\n            level.append(node.val)\n            if node.left:\n                q.append(node.left)\n            if node.right:\n                q.append(node.right)\n        result.append(level)\n    return result\n\nroot = None\nfor v in [5, 3, 8, 1, 4, 7]:\n    root = insert(root, v)\nlevel_order(root)\n"}, {"category": "Trees", "title": "Validate BST", "difficulty": "Medium", "statement": "Check whether a binary tree is a valid BST by passing down allowed (min, max) bounds.", "hints": ["Each node must lie strictly within an inherited range.", "Going left tightens the max; going right tightens the min."], "complexity": "Time O(n) \u00b7 Space O(h)", "mistakes": ["Only comparing a node to its direct children, not ancestors.", "Using <= where strict < is required."], "code": "class TreeNode:\n    def __init__(self, val):\n        self.val = val\n        self.left = None\n        self.right = None\n\ndef insert(root, val):\n    if root is None:\n        return TreeNode(val)\n    if val < root.val:\n        root.left = insert(root.left, val)\n    else:\n        root.right = insert(root.right, val)\n    return root\n\ndef is_bst(node, lo, hi):\n    if node is None:\n        return True\n    if not (lo < node.val < hi):\n        return False\n    return is_bst(node.left, lo, node.val) and is_bst(node.right, node.val, hi)\n\nroot = None\nfor v in [5, 3, 8, 1, 4]:\n    root = insert(root, v)\nis_bst(root, float('-inf'), float('inf'))\n"}, {"category": "Graphs", "title": "Has Path (DFS)", "difficulty": "Easy", "statement": "Determine whether a path exists between two nodes in a directed graph using depth-first search.", "hints": ["Recurse into neighbors, marking visited.", "Return True as soon as the target is reached."], "complexity": "Time O(V + E) \u00b7 Space O(V)", "mistakes": ["No visited set \u2192 infinite loop on cycles.", "Returning too early before exploring all branches."], "code": "def has_path(graph, src, dst, visited):\n    if src == dst:\n        return True\n    visited.append(src)\n    for nb in graph[src]:\n        if nb not in visited:\n            if has_path(graph, nb, dst, visited):\n                return True\n    return False\n\ng = {0: [1, 2], 1: [3], 2: [3], 3: [4], 4: []}\nseen = []\nhas_path(g, 0, 4, seen)\n"}, {"category": "Graphs", "title": "Topological Sort (Kahn)", "difficulty": "Medium", "statement": "Order tasks so every dependency comes first, by repeatedly removing nodes with no remaining incoming edges.", "hints": ["Track in-degree for every node.", "Start with in-degree 0 nodes; decrement neighbors as you remove."], "complexity": "Time O(V + E) \u00b7 Space O(V)", "mistakes": ["Not detecting cycles (output shorter than node count).", "Forgetting to enqueue newly-zero in-degree nodes."], "code": "from collections import deque\n\ndef topo_sort(graph):\n    indeg = {u: 0 for u in graph}\n    for u in graph:\n        for v in graph[u]:\n            indeg[v] += 1\n    q = deque([u for u in graph if indeg[u] == 0])\n    order = []\n    while q:\n        u = q.popleft()\n        order.append(u)\n        for v in graph[u]:\n            indeg[v] -= 1\n            if indeg[v] == 0:\n                q.append(v)\n    return order\n\ng = {0: [1, 2], 1: [3], 2: [3], 3: []}\ntopo_sort(g)\n"}];

// language support matrix — honest about what runs in-browser vs needs a backend
const LANGS = [
  { id: "python", label: "Python", live: true },
  { id: "javascript", label: "JavaScript", live: true },
  { id: "c", label: "C", live: false },
  { id: "cpp", label: "C++", live: false },
  { id: "java", label: "Java", live: false },
];

const CATS = ["Arrays", "Stacks & Queues", "Linked Lists", "Trees", "Graphs", "Dynamic Programming"];
const CAT_ACCENT = {
  "Arrays": "#5ed4ff", "Stacks & Queues": "#ffb454", "Linked Lists": "#5eebb0",
  "Trees": "#9d7cff", "Graphs": "#ff6b8a", "Dynamic Programming": "#ffd65e",
};
const DIFF_COLOR = { "Easy": "#5eebb0", "Medium": "#ffb454", "Hard": "#ff6b8a" };

const C = {
  bg: "#070a0e", panel: "#0b0f14", panel2: "#0e1116", line: "#1a212b",
  border: "#20262e", border2: "#2a323d", text: "#cdd6e0", dim: "#8b97a6",
  faint: "#3a434f", ink: "#eef3f8", a1: "#5ed4ff", a2: "#ffb454",
  a3: "#9d7cff", a4: "#5eebb0", a5: "#ff6b8a",
};

/* ── Pyodide ─────────────────────────────────────────────────────────────── */
function usePyodide() {
  const [py, setPy] = useState(null);
  const [status, setStatus] = useState("idle");
  const started = useRef(false);
  const load = useCallback(async () => {
    if (started.current) return;
    started.current = true;
    setStatus("loading");
    try {
      if (!window.loadPyodide) {
        await new Promise((res, rej) => {
          const s = document.createElement("script");
          s.src = "https://cdn.jsdelivr.net/pyodide/v0.26.2/full/pyodide.js";
          s.onload = res; s.onerror = rej; document.head.appendChild(s);
        });
      }
      const p = await window.loadPyodide({ indexURL: "https://cdn.jsdelivr.net/pyodide/v0.26.2/full/" });
      p.runPython(TRACER_PY);
      setPy(p); setStatus("ready");
    } catch (e) { console.error(e); setStatus("error"); }
  }, []);
  return { py, status, load };
}

/* ── JavaScript tracer (loads acorn + astring from CDN, builds tracer) ────── */
function useJsTracer() {
  const [tracer, setTracer] = useState(null);
  const [status, setStatus] = useState("idle");
  const started = useRef(false);
  const load = useCallback(async () => {
    if (started.current) return;
    started.current = true;
    setStatus("loading");
    try {
      const loadScript = (src) => new Promise((res, rej) => {
        const s = document.createElement("script"); s.src = src; s.onload = res; s.onerror = rej; document.head.appendChild(s);
      });
      if (!window.acorn) await loadScript("https://cdn.jsdelivr.net/npm/acorn@8.11.3/dist/acorn.min.js");
      if (!window.astring) await loadScript("https://cdn.jsdelivr.net/npm/astring@1.8.6/dist/astring.min.js");
      // eslint-disable-next-line no-new-func
      const factory = new Function("acornArg", "astringArg", JS_TRACER_SRC + "; return buildJsTracer(acornArg, astringArg);");
      const t = factory(window.acorn, window.astring);
      setTracer(t); setStatus("ready");
    } catch (e) { console.error(e); setStatus("error"); }
  }, []);
  return { tracer, status, load };
}

/* ── renderers (by structure tag) ────────────────────────────────────────── */
function fmt(snap) {
  if (!snap) return "·";
  if (snap.value !== undefined) return String(snap.value);
  if (snap.type === "null") return "None";
  if (snap.class) return snap.class;
  return snap.type || "·";
}
function Box({ children, top, accent, dim }) {
  return (
    <div className="font-mono text-sm rounded-sm text-center transition-all duration-300"
      style={{ padding: "8px 6px", minWidth: 34,
        background: top ? accent : dim ? "#10151b" : "#1a212b",
        color: top ? "#0a0d11" : "#cdd6e0",
        border: `1px solid ${top ? accent : C.border2}`,
        transform: top ? "scale(1.06)" : "scale(1)",
        boxShadow: top ? `0 0 14px ${accent}66` : "none", fontWeight: top ? 700 : 400 }}>{children}</div>
  );
}
function ArrayView({ snap, accent = C.a1, highlight = [] }) {
  const items = snap?.items || [];
  return (
    <div className="flex items-end gap-1.5 flex-wrap">
      {items.map((it, i) => (
        <div key={i} className="flex flex-col items-center gap-1">
          <Box top={highlight.includes(i)} accent={accent}>{fmt(it)}</Box>
          <span className="font-mono text-[9px]" style={{ color: C.faint }}>{i}</span>
        </div>
      ))}
      {items.length === 0 && <span className="font-mono text-[10px]" style={{ color: C.faint }}>empty</span>}
    </div>
  );
}
function StackView({ snap, accent = C.a1, label }) {
  const items = snap?.items || [];
  return (
    <div className="flex flex-col items-center gap-2">
      {label && <div className="text-[11px] uppercase tracking-[0.2em] font-mono" style={{ color: accent }}>{label}</div>}
      <div className="relative w-24 flex flex-col-reverse items-center rounded-sm p-1.5 gap-1.5"
        style={{ minHeight: 130, background: C.panel2, border: `1px solid ${C.border}` }}>
        <div className="absolute bottom-0 left-0 right-0 h-[3px]" style={{ background: accent, opacity: 0.5 }} />
        {items.length === 0 && <div className="text-[10px] py-2 font-mono self-center" style={{ color: C.faint }}>empty</div>}
        {items.map((it, i) => (<div key={i} className="w-full"><Box top={i === items.length - 1} accent={accent}>{fmt(it)}</Box></div>))}
      </div>
      <div className="text-[9px] font-mono" style={{ color: C.dim }}>top ↑</div>
    </div>
  );
}
function LinkedListView({ snap, accent = C.a4 }) {
  const nodes = []; let cur = snap, guard = 0;
  while (cur && cur.fields && guard++ < 60) {
    nodes.push(cur.fields.val ? fmt(cur.fields.val) : "·");
    const nx = cur.fields.next;
    cur = nx && nx.type && nx.type !== "null" ? nx : null;
  }
  return (
    <div className="flex items-center gap-1 flex-wrap">
      {nodes.map((v, i) => (
        <React.Fragment key={i}>
          <div className="font-mono text-sm rounded-sm px-3 py-2" style={{ background: "#1a212b", border: `1px solid ${accent}`, color: C.text }}>{v}</div>
          {i < nodes.length - 1 && <span style={{ color: accent }}>→</span>}
        </React.Fragment>
      ))}
      <span className="font-mono text-xs ml-1" style={{ color: C.faint }}>→ null</span>
    </div>
  );
}
function treeDepth(n, g = 0) {
  if (!n || !n.fields || g > 30) return 0;
  const l = n.fields.left, r = n.fields.right;
  return 1 + Math.max(l && l.fields ? treeDepth(l, g + 1) : 0, r && r.fields ? treeDepth(r, g + 1) : 0);
}
function TreeNodeSVG({ node, x, y, dx, accent }) {
  if (!node || !node.fields) return null;
  const val = node.fields.val ? fmt(node.fields.val) : "·";
  const childY = y + 56;
  const l = node.fields.left, r = node.fields.right;
  const lx = x - dx, rx = x + dx;
  return (
    <g>
      {l && l.fields && <line x1={x} y1={y} x2={lx} y2={childY} stroke={C.border2} strokeWidth="1.5" />}
      {r && r.fields && <line x1={x} y1={y} x2={rx} y2={childY} stroke={C.border2} strokeWidth="1.5" />}
      {l && l.fields && <TreeNodeSVG node={l} x={lx} y={childY} dx={dx / 1.8} accent={accent} />}
      {r && r.fields && <TreeNodeSVG node={r} x={rx} y={childY} dx={dx / 1.8} accent={accent} />}
      <circle cx={x} cy={y} r="15" fill="#1a212b" stroke={accent} strokeWidth="1.5" />
      <text x={x} y={y + 4} textAnchor="middle" fontSize="12" fontFamily="monospace" fill={C.text}>{val}</text>
    </g>
  );
}
function TreeView({ snap, accent = C.a3 }) {
  const d = treeDepth(snap);
  const w = Math.max(260, Math.pow(2, Math.min(d, 4)) * 44);
  const h = Math.max(80, d * 56 + 30);
  return (<svg width="100%" viewBox={`0 0 ${w} ${h}`} style={{ maxHeight: 240 }}><TreeNodeSVG node={snap} x={w / 2} y={22} dx={w / 4} accent={accent} /></svg>);
}
function GraphView({ snap, accent = C.a5, visited = [] }) {
  const entries = snap?.entries || [];
  const n = entries.length;
  if (n === 0) return <span className="font-mono text-[10px]" style={{ color: C.faint }}>empty graph</span>;
  const R = 80, cx = 130, cy = 100, pos = {};
  entries.forEach((e, i) => { const ang = (i / n) * 2 * Math.PI - Math.PI / 2; pos[e.key] = { x: cx + R * Math.cos(ang), y: cy + R * Math.sin(ang) }; });
  const edges = [];
  entries.forEach((e) => (e.value?.items || []).forEach((nb) => { const k = String(nb.value); if (pos[k]) edges.push([e.key, k]); }));
  return (
    <svg width="100%" viewBox="0 0 260 200" style={{ maxHeight: 240 }}>
      <defs><marker id="arr" markerWidth="6" markerHeight="6" refX="9" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6" fill={C.border2} /></marker></defs>
      {edges.map(([a, b], i) => (<line key={i} x1={pos[a].x} y1={pos[a].y} x2={pos[b].x} y2={pos[b].y} stroke={C.border2} strokeWidth="1.2" markerEnd="url(#arr)" />))}
      {entries.map((e) => {
        const v = visited.includes(Number(e.key)) || visited.includes(e.key);
        return (<g key={e.key}>
          <circle cx={pos[e.key].x} cy={pos[e.key].y} r="15" fill={v ? accent : "#1a212b"} stroke={accent} strokeWidth="1.5" />
          <text x={pos[e.key].x} y={pos[e.key].y + 4} textAnchor="middle" fontSize="12" fontFamily="monospace" fill={v ? "#0a0d11" : C.text}>{e.key}</text>
        </g>);
      })}
    </svg>
  );
}
function MapView({ snap }) {
  return (<div className="flex flex-col gap-1">{(snap.entries || []).map((e, i) => (
    <div key={i} className="font-mono text-xs flex gap-2"><span style={{ color: C.a1 }}>{e.key}</span><span style={{ color: C.faint }}>:</span><span style={{ color: C.text }}>{fmt(e.value)}</span></div>))}</div>);
}
function renderValue(snap, ctx = {}) {
  if (!snap) return null;
  switch (snap.type) {
    case "array": case "tuple": case "set": return <ArrayView snap={snap} highlight={ctx.highlight} accent={ctx.accent} />;
    case "stack": case "queue": return <StackView snap={snap} accent={ctx.accent} />;
    case "linkedlist_node": return <LinkedListView snap={snap} />;
    case "tree_node": return <TreeView snap={snap} />;
    case "map":
      if ((snap.entries || []).every((e) => e.value?.type === "array")) return <GraphView snap={snap} visited={ctx.visited} />;
      return <MapView snap={snap} />;
    default: return null;
  }
}

/* ── Stack + Heap view (Python-Tutor style: frames left, heap right, arrows) ─ */
// Collect every object-with-id reachable from the step's locals.
function collectHeap(locals) {
  const heap = new Map(); // id -> snap
  const SKIP = new Set(["type", "function", "getset_descriptor", "builtin_function_or_method", "method", "module", "classobj"]);
  const walk = (s) => {
    if (!s || typeof s !== "object") return;
    if (SKIP.has(s.class) || SKIP.has(s.type)) return;
    if (s.id != null && !heap.has(s.id)) {
      heap.set(s.id, s);
      (s.items || []).forEach(walk);
      (s.entries || []).forEach((e) => walk(e.value));
      Object.values(s.fields || {}).forEach(walk);
    }
  };
  // skip class definitions in scope (uppercase names) — they aren't data
  Object.entries(locals || {}).forEach(([k, v]) => { if (!/^[A-Z]/.test(k)) walk(v); });
  return heap;
}
function isPrimitive(s) { return s && (s.type === "number" || s.type === "string" || s.type === "bool" || s.type === "null"); }

function HeapView({ step }) {
  const locals = step?.locals || {};
  const heap = useMemo(() => collectHeap(locals), [locals]);
  const heapArr = Array.from(heap.values());
  const refY = useRef({});

  // a heap object box
  const HeapObj = ({ snap }) => {
    if (snap.type === "array" || snap.type === "tuple" || snap.type === "set") {
      return (
        <div className="flex">
          {(snap.items || []).map((it, i) => (
            <div key={i} className="border font-mono text-[12px] text-center" style={{ borderColor: C.border2, minWidth: 30, padding: "5px 6px", color: isPrimitive(it) ? C.text : C.a3 }}>
              {isPrimitive(it) ? fmt(it) : "•"}
            </div>
          ))}
          {(!snap.items || !snap.items.length) && <span className="font-mono text-[10px] px-2 py-1" style={{ color: C.faint }}>[]</span>}
        </div>
      );
    }
    // object / node / tree_node
    return (
      <div className="rounded-sm" style={{ border: `1px solid ${C.a3}66` }}>
        <div className="font-mono text-[9px] px-2 py-0.5" style={{ background: `${C.a3}22`, color: C.a3 }}>{snap.class || "object"}</div>
        <div className="p-1.5 flex flex-col gap-1">
          {Object.entries(snap.fields || {}).map(([k, v]) => (
            <div key={k} className="font-mono text-[11px] flex gap-2">
              <span style={{ color: C.dim }}>{k}</span>
              <span style={{ color: isPrimitive(v) ? C.text : C.a3 }}>{isPrimitive(v) ? fmt(v) : v.type === "null" ? "None" : "→"}</span>
            </div>
          ))}
        </div>
      </div>
    );
  };

  return (
    <div className="grid grid-cols-[1fr_1.2fr] gap-3">
      {/* frame / variables */}
      <div>
        <div className="font-mono text-[9px] uppercase tracking-[0.15em] mb-1.5" style={{ color: C.faint }}>frame · {step.function}</div>
        <div className="rounded-sm p-2 flex flex-col gap-1" style={{ background: C.panel2, border: `1px solid ${C.border}` }}>
          {Object.entries(locals).filter(([k]) => !/^[A-Z]/.test(k)).map(([k, v]) => (
            <div key={k} className="font-mono text-[11px] flex items-center gap-2">
              <span style={{ color: step.changed?.includes(k) ? C.a2 : C.dim }}>{k}</span>
              <span style={{ color: C.faint }}>=</span>
              {isPrimitive(v) ? <span style={{ color: step.changed?.includes(k) ? C.a2 : C.text }}>{fmt(v)}</span>
                : <span style={{ color: C.a3 }}>→ {v.class || v.type}</span>}
            </div>
          ))}
          {Object.keys(locals).filter((k) => !/^[A-Z]/.test(k)).length === 0 && <span className="font-mono text-[10px]" style={{ color: C.faint }}>no locals</span>}
        </div>
      </div>
      {/* heap */}
      <div>
        <div className="font-mono text-[9px] uppercase tracking-[0.15em] mb-1.5" style={{ color: C.faint }}>heap</div>
        <div className="flex flex-col gap-2">
          {heapArr.length === 0 && <span className="font-mono text-[10px]" style={{ color: C.faint }}>no objects</span>}
          {heapArr.map((s) => <div key={s.id}><HeapObj snap={s} /></div>)}
        </div>
      </div>
    </div>
  );
}

/* ── explanation ─────────────────────────────────────────────────────────── */
function explain(step) {
  const code = (step.code || "").trim();
  if (step.event === "call") return `Entering ${step.function}() — a new frame is pushed onto the call stack.`;
  if (step.event === "return") return (step.note || "").replace("← ", "Returning from ");
  if (step.event === "exception") return step.note;
  if (/append|push/.test(code)) return "An element is added to the end of this structure.";
  if (/popleft/.test(code)) return "Dequeue: the front element leaves the queue (FIFO).";
  if (/pop/.test(code)) return "An element is removed from the top/end of this structure.";
  if (/\.next\s*=/.test(code)) return "A linked-list pointer is reassigned — the chain is being rewired.";
  if (/slow|fast/.test(code)) return "Two-pointer step — slow and fast advance at different speeds.";
  if (/mid\s*=/.test(code)) return "Computing the midpoint to halve the search range.";
  if (/insert/.test(code)) return "Inserting into the structure; a BST walks left/right by comparison.";
  if (/< root\.val|val <|a\[mid\]/.test(code)) return "Comparison decides the next branch or pointer move.";
  if (/visited/.test(code)) return "Traversal bookkeeping — marking or checking a node as seen.";
  if (/while|for/.test(code)) return "Loop iteration — watch the changed variables for progress.";
  if (/=/.test(code)) return "Assignment — a variable's value is being set or updated.";
  return "Executing this line.";
}

/* ── small UI bits ───────────────────────────────────────────────────────── */
function Pill({ children, color }) {
  return <span className="font-mono text-[10px] px-2 py-0.5 rounded-full" style={{ color, border: `1px solid ${color}55` }}>{children}</span>;
}

/* ── shared: extract visualizable structures from a step ─────────────────── */
function extractStructures(step) {
  if (!step) return [];
  const out = [], locals = step.locals || {};
  const scopes = { ...locals };
  if (locals.self?.fields) Object.assign(scopes, locals.self.fields);
  const visited = (scopes.visited?.items || scopes.order?.items || []).map((x) => x.value);
  for (const [name, snap] of Object.entries(scopes)) {
    if (!snap || name === "self") continue;
    const el = renderValue(snap, { accent: name.includes("out") ? C.a2 : C.a1, visited });
    if (el) out.push({ name, el });
  }
  return out;
}

/* ── detect the entry function + params from pasted code ─────────────────── */
function detectEntry(code, lang) {
  try {
    if (lang === "javascript" && window.acorn) {
      const ast = window.acorn.parse(code, { ecmaVersion: 2022 });
      const fn = ast.body.find((n) => n.type === "FunctionDeclaration");
      if (fn) return { name: fn.id.name, params: fn.params.map((p) => p.name || "arg") };
    }
    if (lang === "python") {
      const m = code.match(/def\s+([A-Za-z_]\w*)\s*\(([^)]*)\)/);
      if (m) {
        const params = m[2].split(",").map((s) => s.trim().split(/[:=]/)[0].trim()).filter((s) => s && s !== "self");
        return { name: m[1], params };
      }
    }
  } catch (e) { /* ignore parse errors during typing */ }
  return null;
}

// build a trailing call to the entry function from user-supplied argument text
function buildCall(entry, argText) {
  if (!entry) return "";
  const args = (argText || "").trim();
  return `\n${entry.name}(${args})\n`;
}

/* ANIMATION LAYER for the general visualizer.
   Dependency-free FLIP animation (no Framer Motion — not reliably importable in
   the artifact sandbox). Elements get stable keys; we measure positions before
   and after a step change and tween the delta with a transform.
   This file is concatenated into the template (not a real import). */

/* ── operation detection: what is this step DOING? ───────────────────────── */
function detectOps(step, prevStep) {
  // returns { reads:Set<string>, writes:Set<string>, kind:string }
  // keyed on "varname[index]" for arrays; kind ∈ read|write|swap|push|pop|none
  const code = (step?.code || "");
  const ops = { reads: new Set(), writes: new Set(), kind: "none", arrayName: null, indices: [] };

  // index expressions like a[j], arr[i+1] — capture the variable and try to
  // resolve simple numeric indices from the *previous* step's locals.
  const idxRe = /([A-Za-z_]\w*)\s*\[\s*([^\]]+?)\s*\]/g;
  const resolve = (expr, locals) => {
    const t = expr.trim();
    if (/^\d+$/.test(t)) return Number(t);
    // single variable index
    if (/^[A-Za-z_]\w*$/.test(t)) {
      const v = locals?.[t];
      if (v && v.type === "number") return v.value;
    }
    // simple var±const
    const m = t.match(/^([A-Za-z_]\w*)\s*([+\-])\s*(\d+)$/);
    if (m) {
      const v = locals?.[m[1]];
      if (v && v.type === "number") return m[2] === "+" ? v.value + Number(m[3]) : v.value - Number(m[3]);
    }
    return null;
  };

  const locals = prevStep?.locals || step?.locals || {};
  let m, touched = [];
  while ((m = idxRe.exec(code))) {
    const arr = m[1], idx = resolve(m[2], locals);
    if (idx != null) touched.push({ arr, idx, raw: m[0] });
  }
  if (touched.length) {
    ops.arrayName = touched[0].arr;
    ops.indices = touched.map((t) => t.idx);
  }

  // classify
  if (/\b\w+\s*,\s*\w+.*=.*\w+\s*,\s*\w+/.test(code) || /swap/i.test(code)) ops.kind = "swap";
  else if (/\.append\(|\.push\(|\.add\(/.test(code)) ops.kind = "push";
  else if (/\.pop\(|popleft/.test(code)) ops.kind = "pop";
  else if (/\[[^\]]+\]\s*=/.test(code)) ops.kind = "write";
  else if (touched.length) ops.kind = "read";

  return ops;
}

/* ── FLIP hook: animate element movement between renders ─────────────────── */
function useFlip(deps) {
  const refs = useRef(new Map());     // key -> DOM node
  const prevRects = useRef(new Map()); // key -> DOMRect

  useLayoutEffect(() => {
    const nodes = refs.current;
    nodes.forEach((node, key) => {
      if (!node) return;
      const newRect = node.getBoundingClientRect();
      const old = prevRects.current.get(key);
      if (old) {
        const dx = old.left - newRect.left;
        const dy = old.top - newRect.top;
        if (Math.abs(dx) > 0.5 || Math.abs(dy) > 0.5) {
          node.style.transition = "none";
          node.style.transform = `translate(${dx}px, ${dy}px)`;
          // force reflow then animate to zero
          // eslint-disable-next-line no-unused-expressions
          node.getBoundingClientRect();
          requestAnimationFrame(() => {
            node.style.transition = "transform 380ms cubic-bezier(.4,0,.2,1)";
            node.style.transform = "";
          });
        }
      }
    });
    // record new positions
    const map = new Map();
    nodes.forEach((node, key) => { if (node) map.set(key, node.getBoundingClientRect()); });
    prevRects.current = map;
  }, deps); // eslint-disable-line react-hooks/exhaustive-deps

  const register = useCallback((key) => (el) => {
    if (el) refs.current.set(key, el); else refs.current.delete(key);
  }, []);
  return register;
}

/* ── animated array: stable keys per slot, flash reads/writes, pulse swaps ── */
function AnimatedArray({ snap, ops, accent = C.a1, prevItems }) {
  const items = snap?.items || [];
  const touched = new Set(ops?.arrayName ? ops.indices : []);
  const writing = ops?.kind === "write" || ops?.kind === "swap";

  return (
    <div className="flex items-end gap-1.5 flex-wrap" style={{ minHeight: 52 }}>
      {items.map((it, i) => {
        const active = touched.has(i);
        const changed = prevItems && JSON.stringify(prevItems[i]) !== JSON.stringify(it);
        const hot = active && writing;
        return (
          <div key={i} className="flex flex-col items-center gap-1">
            <div className="font-mono text-sm rounded-sm text-center"
              style={{
                padding: "9px 8px", minWidth: 36,
                background: hot ? accent : active ? `${accent}33` : "#1a212b",
                color: hot ? "#0a0d11" : "#cdd6e0",
                border: `1px solid ${active ? accent : C.border2}`,
                transform: changed ? "translateY(-6px) scale(1.1)" : active ? "scale(1.05)" : "scale(1)",
                boxShadow: hot ? `0 0 18px ${accent}aa` : active ? `0 0 10px ${accent}55` : "none",
                fontWeight: active ? 700 : 400,
                transition: "all 320ms cubic-bezier(.4,0,.2,1)",
              }}>
              {fmt(it)}
            </div>
            <span className="font-mono text-[9px]" style={{ color: active ? accent : C.faint }}>{i}</span>
          </div>
        );
      })}
      {items.length === 0 && <span className="font-mono text-[10px]" style={{ color: C.faint }}>empty</span>}
    </div>
  );
}

/* ── animated stack: items slide in/out from the top ─────────────────────── */
function AnimatedStack({ snap, accent = C.a1, op }) {
  const items = snap?.items || [];
  return (
    <div className="flex flex-col items-center gap-2">
      <div className="relative w-24 flex flex-col-reverse items-center rounded-sm p-1.5 gap-1.5"
        style={{ minHeight: 130, background: C.panel2, border: `1px solid ${C.border}` }}>
        <div className="absolute bottom-0 left-0 right-0 h-[3px]" style={{ background: accent, opacity: 0.5 }} />
        {items.length === 0 && <div className="text-[10px] py-2 font-mono self-center" style={{ color: C.faint }}>empty</div>}
        {items.map((it, i) => {
          const top = i === items.length - 1;
          const justChanged = top && (op === "push" || op === "pop");
          return (
            <div key={`${i}-${fmt(it)}`} className="w-full font-mono text-sm rounded-sm text-center"
              style={{
                padding: "8px 6px",
                background: top ? accent : "#1a212b",
                color: top ? "#0a0d11" : "#cdd6e0",
                border: `1px solid ${top ? accent : C.border2}`,
                fontWeight: top ? 700 : 400,
                transform: justChanged ? "scale(1.08)" : "scale(1)",
                boxShadow: top ? `0 0 14px ${accent}66` : "none",
                transition: "all 300ms cubic-bezier(.4,0,.2,1)",
                animation: justChanged && op === "push" ? "popIn 360ms ease" : "none",
              }}>{fmt(it)}</div>
          );
        })}
      </div>
      <div className="text-[9px] font-mono" style={{ color: C.dim }}>top ↑</div>
    </div>
  );
}

/* ── animated heap with reference arrows (frame → heap, field → heap) ────── */
function isPrim(s) { return s && (s.type === "number" || s.type === "string" || s.type === "bool" || s.type === "null"); }

function AnimatedHeap({ step }) {
  const locals = step?.locals || {};
  const heap = useMemo(() => {
    const m = new Map();
    const SKIP = new Set(["type", "function", "getset_descriptor", "builtin_function_or_method", "method", "module"]);
    const walk = (s) => {
      if (!s || typeof s !== "object") return;
      if (SKIP.has(s.class) || SKIP.has(s.type)) return;
      if (s.id != null && !m.has(s.id)) {
        m.set(s.id, s);
        (s.items || []).forEach(walk);
        (s.entries || []).forEach((e) => walk(e.value));
        Object.values(s.fields || {}).forEach(walk);
      }
    };
    Object.entries(locals).forEach(([k, v]) => { if (!/^[A-Z]/.test(k)) walk(v); });
    return m;
  }, [locals]);

  const containerRef = useRef(null);
  const anchorRefs = useRef(new Map()); // anchorKey -> node (source of a pointer)
  const targetRefs = useRef(new Map()); // objId -> node (heap object)
  const [arrows, setArrows] = useState([]);

  // gather pointer relationships: (anchorKey, targetId)
  const links = [];
  Object.entries(locals).forEach(([k, v]) => {
    if (/^[A-Z]/.test(k)) return;
    if (v && v.id != null && !isPrim(v)) links.push({ anchor: `var:${k}`, target: v.id });
  });
  heap.forEach((obj, id) => {
    Object.entries(obj.fields || {}).forEach(([fk, fv]) => {
      if (fv && fv.id != null && !isPrim(fv)) links.push({ anchor: `field:${id}:${fk}`, target: fv.id });
    });
  });

  useLayoutEffect(() => {
    const cont = containerRef.current;
    if (!cont) return;
    const base = cont.getBoundingClientRect();
    const next = [];
    links.forEach(({ anchor, target }) => {
      const a = anchorRefs.current.get(anchor);
      const t = targetRefs.current.get(target);
      if (!a || !t) return;
      const ar = a.getBoundingClientRect(), tr = t.getBoundingClientRect();
      next.push({
        x1: ar.right - base.left, y1: ar.top + ar.height / 2 - base.top,
        x2: tr.left - base.left, y2: tr.top + tr.height / 2 - base.top,
        key: `${anchor}->${target}`,
      });
    });
    setArrows(next);
  }, [step]); // eslint-disable-line react-hooks/exhaustive-deps

  const regAnchor = (key) => (el) => { if (el) anchorRefs.current.set(key, el); else anchorRefs.current.delete(key); };
  const regTarget = (id) => (el) => { if (el) targetRefs.current.set(id, el); else targetRefs.current.delete(id); };

  const heapArr = Array.from(heap.values());

  return (
    <div ref={containerRef} className="relative grid grid-cols-[1fr_1.3fr] gap-6">
      {/* arrows overlay */}
      <svg className="absolute inset-0 pointer-events-none" style={{ width: "100%", height: "100%", overflow: "visible" }}>
        <defs><marker id="hp" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill={C.a3} /></marker></defs>
        {arrows.map((a) => {
          const mx = (a.x1 + a.x2) / 2;
          return <path key={a.key} d={`M ${a.x1} ${a.y1} C ${mx} ${a.y1}, ${mx} ${a.y2}, ${a.x2 - 8} ${a.y2}`}
            fill="none" stroke={C.a3} strokeWidth="1.5" markerEnd="url(#hp)" style={{ transition: "all 380ms cubic-bezier(.4,0,.2,1)" }} opacity="0.85" />;
        })}
      </svg>

      {/* frame */}
      <div className="relative z-10">
        <div className="font-mono text-[9px] uppercase tracking-[0.15em] mb-1.5" style={{ color: C.faint }}>frame · {step.function}</div>
        <div className="rounded-sm p-2 flex flex-col gap-1.5" style={{ background: C.panel2, border: `1px solid ${C.border}` }}>
          {Object.entries(locals).filter(([k]) => !/^[A-Z]/.test(k)).map(([k, v]) => (
            <div key={k} className="font-mono text-[11px] flex items-center gap-2">
              <span style={{ color: step.changed?.includes(k) ? C.a2 : C.dim }}>{k}</span>
              <span style={{ color: C.faint }}>=</span>
              {isPrim(v)
                ? <span style={{ color: step.changed?.includes(k) ? C.a2 : C.text, transition: "color 300ms" }}>{fmt(v)}</span>
                : <span ref={regAnchor(`var:${k}`)} className="inline-block w-2 h-2 rounded-full" style={{ background: C.a3 }} />}
            </div>
          ))}
          {Object.keys(locals).filter((k) => !/^[A-Z]/.test(k)).length === 0 && <span className="font-mono text-[10px]" style={{ color: C.faint }}>no locals</span>}
        </div>
      </div>

      {/* heap */}
      <div className="relative z-10">
        <div className="font-mono text-[9px] uppercase tracking-[0.15em] mb-1.5" style={{ color: C.faint }}>heap</div>
        <div className="flex flex-col gap-2.5">
          {heapArr.length === 0 && <span className="font-mono text-[10px]" style={{ color: C.faint }}>no objects</span>}
          {heapArr.map((s) => (
            <div key={s.id} ref={regTarget(s.id)} className="self-start rounded-sm"
              style={{ border: `1px solid ${C.a3}55`, animation: "popIn 360ms ease" }}>
              {(s.type === "array" || s.type === "tuple" || s.type === "set") ? (
                <div className="flex">
                  {(s.items || []).map((it, i) => (
                    <div key={i} className="border font-mono text-[12px] text-center" style={{ borderColor: C.border2, minWidth: 30, padding: "5px 7px", color: isPrim(it) ? C.text : C.a3 }}>{isPrim(it) ? fmt(it) : "•"}</div>
                  ))}
                  {(!s.items || !s.items.length) && <span className="font-mono text-[10px] px-2 py-1" style={{ color: C.faint }}>[]</span>}
                </div>
              ) : (
                <div>
                  <div className="font-mono text-[9px] px-2 py-0.5" style={{ background: `${C.a3}22`, color: C.a3 }}>{s.class || "object"}</div>
                  <div className="p-1.5 flex flex-col gap-1">
                    {Object.entries(s.fields || {}).map(([k, v]) => (
                      <div key={k} className="font-mono text-[11px] flex items-center gap-2">
                        <span style={{ color: C.dim }}>{k}</span>
                        {isPrim(v)
                          ? <span style={{ color: C.text }}>{fmt(v)}</span>
                          : v.type === "null" || v.id == null
                            ? <span style={{ color: C.faint }}>None</span>
                            : <span ref={regAnchor(`field:${s.id}:${k}`)} className="inline-block w-2 h-2 rounded-full" style={{ background: C.a3 }} />}
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

/* ── animated 2D matrix (DP tables): highlight the cell being written ────── */
function AnimatedMatrix({ snap, prev, accent = "#ffd65e" }) {
  const rows = snap?.items || [];
  const prevRows = prev?.items || [];
  // find the cell that changed vs previous step
  let hot = null;
  for (let r = 0; r < rows.length; r++) {
    const cur = rows[r]?.items || [];
    const pr = prevRows[r]?.items || [];
    for (let c = 0; c < cur.length; c++) {
      if (JSON.stringify(cur[c]) !== JSON.stringify(pr[c])) { hot = [r, c]; break; }
    }
    if (hot) break;
  }
  return (
    <div className="inline-flex flex-col gap-1">
      {rows.map((row, r) => (
        <div key={r} className="flex gap-1">
          {(row.items || []).map((cell, c) => {
            const isHot = hot && hot[0] === r && hot[1] === c;
            return (
              <div key={c} className="font-mono text-[11px] text-center rounded-sm"
                style={{
                  minWidth: 26, padding: "5px 4px",
                  background: isHot ? accent : "#141a22",
                  color: isHot ? "#0a0d11" : C.text,
                  border: `1px solid ${isHot ? accent : C.border2}`,
                  transform: isHot ? "scale(1.15)" : "scale(1)",
                  boxShadow: isHot ? `0 0 14px ${accent}aa` : "none",
                  fontWeight: isHot ? 700 : 400,
                  transition: "all 300ms cubic-bezier(.4,0,.2,1)",
                }}>{fmt(cell)}</div>
            );
          })}
        </div>
      ))}
    </div>
  );
}

// is this snapshot a 2D array (array of arrays)?
function is2D(snap) {
  return snap && (snap.type === "array") && (snap.items || []).length > 0 &&
    snap.items.every((it) => it && it.type === "array");
}


/* ── GENERAL VISUALIZER ──────────────────────────────────────────────────── */
const STARTER = {
  python: `def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return [-1, -1]
`,
  javascript: `function bubbleSort(arr) {
  let n = arr.length;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n - 1 - i; j++) {
      if (arr[j] > arr[j + 1]) {
        let t = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = t;
      }
    }
  }
  return arr;
}
`,
};
const STARTER_ARGS = { python: "[2, 7, 11, 15], 9", javascript: "[5, 2, 4, 1, 3]" };

function GeneralVisualizer({ onHome }) {
  const [lang, setLang] = useState("python");
  const [code, setCode] = useState(STARTER.python);
  const [problemText, setProblemText] = useState("");
  const [argText, setArgText] = useState(STARTER_ARGS.python);
  const [trace, setTrace] = useState(null);
  const [idx, setIdx] = useState(0);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(1);
  const [running, setRunning] = useState(false);
  const [vizMode, setVizMode] = useState("structures"); // structures | heap
  const timer = useRef(null);

  const { py, status: pyStatus, load: loadPy } = usePyodide();
  const { tracer: jsTracer, status: jsStatus, load: loadJs } = useJsTracer();

  const live = LANGS.find((l) => l.id === lang)?.live;
  const status = lang === "python" ? pyStatus : lang === "javascript" ? jsStatus : "n/a";

  useEffect(() => {
    if (lang === "python") loadPy();
    if (lang === "javascript") loadJs();
  }, [lang, loadPy, loadJs]);

  useEffect(() => {
    if (playing && trace) {
      timer.current = setTimeout(() => setIdx((i) => (i + 1 < trace.steps.length ? i + 1 : (setPlaying(false), i))), 850 / speed);
      return () => clearTimeout(timer.current);
    }
  }, [playing, idx, speed, trace]);

  const entry = useMemo(() => detectEntry(code, lang), [code, lang]);

  const switchLang = (id) => {
    setLang(id); setTrace(null); setIdx(0);
    if (STARTER[id]) { setCode(STARTER[id]); setArgText(STARTER_ARGS[id] || ""); }
  };

  const run = useCallback(async () => {
    if (!live) return;
    setRunning(true); setPlaying(false); setTrace(null); setIdx(0);
    try {
      if (lang === "python") {
        if (!py) { setRunning(false); return; }
        const fullCode = code + buildCall(entry, argText);
        py.globals.set("__src__", fullCode);
        const res = py.runPython("import json; json.dumps(trace_source(__src__))");
        setTrace(JSON.parse(res));
      } else if (lang === "javascript") {
        if (!jsTracer) { setRunning(false); return; }
        const fullCode = code + buildCall(entry, argText);
        setTrace(jsTracer.run(fullCode));
      }
    } catch (e) {
      setTrace({ steps: [], error: { type: "Error", message: String(e) }, source: code });
    }
    setRunning(false);
  }, [lang, py, jsTracer, code, argText, entry, live]);

  const step = trace?.steps?.[idx];
  const prevStep = idx > 0 ? trace?.steps?.[idx - 1] : null;
  const ops = useMemo(() => detectOps(step, prevStep), [step, prevStep]);
  const flipReg = useFlip([idx]);
  // animation-aware structure list: name + snap + previous snap
  const animStructures = useMemo(() => {
    if (!step) return [];
    const out = [], locals = step.locals || {};
    const prevLocals = prevStep?.locals || {};
    const scopes = { ...locals }, prevScopes = { ...prevLocals };
    if (locals.self?.fields) Object.assign(scopes, locals.self.fields);
    if (prevLocals.self?.fields) Object.assign(prevScopes, prevLocals.self.fields);
    for (const [name, snap] of Object.entries(scopes)) {
      if (!snap || name === "self" || /^[A-Z]/.test(name)) continue;
      if (["array", "tuple", "set", "stack", "queue", "linkedlist_node", "tree_node", "map"].includes(snap.type)) {
        out.push({ name, snap, prev: prevScopes[name] });
      }
    }
    return out;
  }, [step, prevStep]);

  return (
    <div className="min-h-screen font-sans" style={{ background: C.bg, color: C.text }}>
      <style>{baseCss}</style>
      <div className="max-w-7xl mx-auto px-5 py-4">
        <div className="flex items-center justify-between border-b pb-3 mb-4" style={{ borderColor: C.line }}>
          <div className="flex items-center gap-3">
            <button onClick={onHome} className="font-mono text-sm" style={{ color: C.ink }}>codeviz <span style={{ color: C.a1 }}>·</span></button>
            <span className="font-mono text-[11px]" style={{ color: C.faint }}>general visualizer</span>
          </div>
          <div className="font-mono text-[11px]" style={{ color: status === "ready" ? C.a4 : C.dim }}>
            {!live ? "● needs backend execution" : status === "loading" ? "● loading runtime…" : status === "ready" ? "● runtime ready" : status === "error" ? "● runtime failed" : "○ idle"}
          </div>
        </div>

        {/* language selector */}
        <div className="flex gap-1.5 flex-wrap mb-4">
          {LANGS.map((l) => (
            <button key={l.id} onClick={() => switchLang(l.id)} className="ctrl"
              style={{ ...(lang === l.id ? { color: C.a1, borderColor: C.a1 } : {}), opacity: l.live ? 1 : 0.5 }}
              title={l.live ? "" : "Runs only with the backend execution service"}>
              {l.label}{!l.live && " ·lock"}
            </button>
          ))}
        </div>

        <div className="grid lg:grid-cols-[1fr_1.1fr] gap-4">
          {/* left: inputs */}
          <div className="flex flex-col gap-3">
            <div>
              <label className="font-mono text-[10px] uppercase tracking-[0.2em] block mb-1.5" style={{ color: C.dim }}>problem statement <span style={{ color: C.faint }}>· optional</span></label>
              <input value={problemText} onChange={(e) => setProblemText(e.target.value)} placeholder="e.g. find two indices that sum to target"
                className="w-full font-sans text-[13px] rounded-md px-3 py-2" style={{ background: C.panel, border: `1px solid ${C.line}`, color: C.text, outline: "none" }} />
            </div>

            <div>
              <label className="font-mono text-[10px] uppercase tracking-[0.2em] block mb-1.5" style={{ color: C.dim }}>your code</label>
              <textarea value={code} onChange={(e) => setCode(e.target.value)} spellCheck={false}
                className="w-full font-mono text-[12.5px] leading-[1.5] rounded-md p-3 resize-none"
                style={{ background: C.panel, border: `1px solid ${C.line}`, color: C.text, minHeight: 240, outline: "none" }} />
            </div>

            {/* input / test case entry */}
            <div className="rounded-md p-3" style={{ background: C.panel, border: `1px solid ${C.line}` }}>
              <div className="flex items-center justify-between mb-2">
                <label className="font-mono text-[10px] uppercase tracking-[0.2em]" style={{ color: C.dim }}>test input <span style={{ color: C.faint }}>· optional</span></label>
                {entry && <span className="font-mono text-[10px]" style={{ color: C.a4 }}>detected: {entry.name}({entry.params.join(", ")})</span>}
              </div>
              {entry
                ? <div className="font-mono text-[12px] flex items-center gap-1.5 flex-wrap">
                    <span style={{ color: C.dim }}>{entry.name}(</span>
                    <input value={argText} onChange={(e) => setArgText(e.target.value)} spellCheck={false} placeholder={entry.params.join(", ")}
                      className="flex-1 min-w-[140px] rounded-sm px-2 py-1" style={{ background: C.panel2, border: `1px solid ${C.border}`, color: C.text, outline: "none" }} />
                    <span style={{ color: C.dim }}>)</span>
                  </div>
                : <input value={argText} onChange={(e) => setArgText(e.target.value)} spellCheck={false} placeholder="no entry function detected — your code runs as-is"
                    className="w-full font-mono text-[12px] rounded-sm px-2 py-1.5" style={{ background: C.panel2, border: `1px solid ${C.border}`, color: C.text, outline: "none" }} />}
              <p className="font-mono text-[10px] mt-2 mb-0" style={{ color: C.faint }}>
                {entry ? "values are passed as arguments to the detected function" : "if your code has a function, its arguments appear here automatically"}
              </p>
            </div>

            <button onClick={run} disabled={!live || status !== "ready" || running} className="font-mono text-sm py-2.5 rounded-md"
              style={{ background: live && status === "ready" ? C.a1 : C.border2, color: "#0a0d11", fontWeight: 600, opacity: running ? 0.6 : 1, cursor: live && status === "ready" ? "pointer" : "not-allowed" }}>
              {!live ? "requires backend execution" : running ? "tracing…" : status === "ready" ? "▶ visualize" : "loading runtime…"}
            </button>

            {!live && (
              <div className="rounded-md p-3 font-mono text-[11px] leading-relaxed" style={{ background: C.panel, border: `1px solid ${C.border2}`, color: C.dim }}>
                {LANGS.find((l) => l.id === lang)?.label} can't execute inside the browser. It compiles/runs only through the codeviz backend execution service (sandboxed per-language workers). Python and JavaScript run live here.
              </div>
            )}
          </div>

          {/* right: visualization */}
          <div className="flex flex-col gap-3">
            {problemText && <div className="rounded-md px-4 py-3 text-[13px]" style={{ background: C.panel, border: `1px solid ${C.line}`, color: C.text }}>{problemText}</div>}

            {!trace && <div className="rounded-md flex items-center justify-center text-center p-10" style={{ background: C.panel, border: `1px dashed ${C.border2}`, minHeight: 280 }}>
              <div><div className="font-mono text-sm mb-2" style={{ color: C.dim }}>{!live ? "select Python or JavaScript to run live" : "paste code, set input, hit visualize"}</div>
              <div className="font-mono text-[11px]" style={{ color: C.faint }}>{live && status !== "ready" ? "runtime is loading…" : "the visualizer infers structures from your variables"}</div></div></div>}

            {trace?.error && <div className="rounded-md p-4 font-mono text-xs" style={{ background: C.panel, border: `1px solid ${C.a5}55`, color: C.a5 }}>{trace.error.type}: {trace.error.message}</div>}

            {trace && step && (<>
              {trace && trace.steps.length > 0 && (
                <div className="rounded-md overflow-hidden" style={{ background: C.panel, border: `1px solid ${C.line}` }}>
                  <div className="px-3 py-2 text-[11px] uppercase tracking-[0.2em] font-mono border-b" style={{ color: C.dim, borderColor: C.line }}>source · line {step.line}</div>
                  <pre className="text-[12px] leading-[1.5] font-mono p-3 m-0 overflow-x-auto" style={{ maxHeight: 200 }}>
                    {(trace.source || code).split("\n").map((ln, i) => {
                      const active = i + 1 === step.line;
                      return (<div key={i} className="flex px-2 -mx-2 rounded-sm transition-colors duration-150" style={{ background: active ? `${C.a1}1a` : "transparent" }}>
                        <span className="w-7 text-right pr-3 select-none inline-block" style={{ color: active ? C.a1 : C.faint }}>{i + 1}</span>
                        <span style={{ color: active ? C.ink : C.dim }}>{ln || " "}</span></div>);
                    })}
                  </pre>
                </div>
              )}
              <div className="rounded-md p-4" style={{ background: C.panel, border: `1px solid ${C.line}`, minHeight: 200 }}>
                <div className="flex items-center justify-between mb-3">
                  <div className="text-[11px] uppercase tracking-[0.2em] font-mono" style={{ color: C.dim }}>{vizMode === "structures" ? "data structures" : "stack & heap"}</div>
                  <div className="flex gap-1">
                    <button onClick={() => setVizMode("structures")} className="ctrl" style={vizMode === "structures" ? { color: C.a1, borderColor: C.a1 } : {}}>structures</button>
                    <button onClick={() => setVizMode("heap")} className="ctrl" style={vizMode === "heap" ? { color: C.a1, borderColor: C.a1 } : {}}>stack & heap</button>
                  </div>
                </div>
                {vizMode === "structures" ? (
                  <div className="flex flex-col gap-5">
                    {animStructures.length === 0 && <div className="font-mono text-[11px]" style={{ color: C.faint }}>no visualizable structure in scope at this step</div>}
                    {animStructures.map(({ name, snap, prev }) => {
                      const isActive = ops.arrayName === name;
                      let el;
                      if (is2D(snap))
                        el = <AnimatedMatrix snap={snap} prev={prev} accent={C.a2} />;
                      else if (["array", "tuple", "set"].includes(snap.type))
                        el = <AnimatedArray snap={snap} ops={isActive ? ops : null} accent={name.includes("out") ? C.a2 : C.a1} prevItems={prev?.items} />;
                      else if (["stack", "queue"].includes(snap.type))
                        el = <AnimatedStack snap={snap} accent={C.a1} op={ops.kind} />;
                      else
                        el = renderValue(snap, { accent: C.a1, visited: (animStructures.find((s) => s.name === "visited" || s.name === "order")?.snap?.items || []).map((x) => x.value) });
                      return (
                        <div key={name} className="flex flex-col gap-2">
                          <div className="font-mono text-[10px] flex items-center gap-2" style={{ color: step.changed?.includes(name) ? C.a2 : C.dim }}>
                            {name}
                            {isActive && ops.kind !== "none" && <span className="px-1.5 py-0.5 rounded-full text-[9px]" style={{ background: `${C.a2}22`, color: C.a2 }}>{ops.kind}{ops.indices.length ? ` [${ops.indices.join(",")}]` : ""}</span>}
                          </div>
                          {el}
                        </div>
                      );
                    })}
                  </div>
                ) : <AnimatedHeap step={step} />}
              </div>
              <div className="rounded-md p-4" style={{ background: C.panel, border: `1px solid ${C.a1}33` }}>
                <div className="text-[11px] uppercase tracking-[0.2em] font-mono mb-2" style={{ color: C.a1 }}>explanation</div>
                <p className="text-[13px] leading-relaxed m-0" style={{ color: C.text }}>{explain(step)}</p>
                {step.note && step.event !== "line" && <p className="font-mono text-[11px] mt-2 mb-0" style={{ color: C.dim }}>{step.note}</p>}
              </div>
              <div className="rounded-md p-3" style={{ background: C.panel, border: `1px solid ${C.line}` }}>
                <div className="text-[11px] uppercase tracking-[0.2em] font-mono mb-2" style={{ color: C.dim }}>variables · {step.function}()</div>
                <div className="flex flex-wrap gap-2">
                  {Object.entries(step.locals || {}).filter(([k]) => k !== "self" && !/^[A-Z]/.test(k)).map(([k, v]) => (
                    <div key={k} className="font-mono text-[11px] px-2 py-1 rounded-sm" style={{ background: C.panel2, border: `1px solid ${step.changed?.includes(k) ? C.a2 : C.border}` }}>
                      <span style={{ color: C.dim }}>{k}=</span><span style={{ color: step.changed?.includes(k) ? C.a2 : C.text }}>{fmt(v)}</span></div>
                  ))}
                </div>
              </div>
            </>)}

            {trace && trace.steps.length > 0 && (
              <div className="flex items-center gap-2 flex-wrap">
                <button onClick={() => { setIdx(0); setPlaying(false); }} className="ctrl">⏮</button>
                <button onClick={() => { setPlaying(false); setIdx((i) => Math.max(0, i - 1)); }} className="ctrl">◂ prev</button>
                <button onClick={() => setPlaying((p) => !p)} className="ctrl" style={{ background: C.a1, color: "#0a0d11", borderColor: C.a1 }}>{playing ? "❚❚" : "▶"}</button>
                <button onClick={() => { setPlaying(false); setIdx((i) => Math.min(trace.steps.length - 1, i + 1)); }} className="ctrl">next ▸</button>
                <button onClick={() => { setIdx(trace.steps.length - 1); setPlaying(false); }} className="ctrl">⏭</button>
                {[0.5, 1, 2, 4].map((s) => (<button key={s} onClick={() => setSpeed(s)} className="ctrl" style={speed === s ? { color: C.a1, borderColor: C.a1 } : {}}>{s}×</button>))}
                <span className="font-mono text-[11px] ml-1" style={{ color: C.faint }}>{idx}/{trace.steps.length - 1}</span>
                <input type="range" min={0} max={trace.steps.length - 1} value={idx} onChange={(e) => { setPlaying(false); setIdx(Number(e.target.value)); }} className="flex-1 min-w-[140px]" style={{ accentColor: C.a1 }} />
              </div>
            )}
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
}

/* ── app ─────────────────────────────────────────────────────────────────── */
export default function App() {
  const [view, setView] = useState("landing"); // landing | library | studio
  const [activeCat, setActiveCat] = useState("Arrays");
  const [problem, setProblem] = useState(null);
  const [code, setCode] = useState("");
  const [trace, setTrace] = useState(null);
  const [idx, setIdx] = useState(0);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(1);
  const [running, setRunning] = useState(false);
  const [tab, setTab] = useState("problem"); // problem | hints | mistakes
  const { py, status, load } = usePyodide();
  const timer = useRef(null);

  useEffect(() => { if (view === "studio") load(); }, [view, load]);
  useEffect(() => {
    if (playing && trace) {
      timer.current = setTimeout(() => setIdx((i) => (i + 1 < trace.steps.length ? i + 1 : (setPlaying(false), i))), 850 / speed);
      return () => clearTimeout(timer.current);
    }
  }, [playing, idx, speed, trace]);

  const openProblem = (p) => { setProblem(p); setCode(p.code); setTrace(null); setIdx(0); setTab("problem"); setView("studio"); };

  const run = useCallback(async () => {
    if (!py) return;
    setRunning(true); setPlaying(false); setTrace(null); setIdx(0);
    try {
      py.globals.set("__src__", code);
      const result = py.runPython("import json; json.dumps(trace_source(__src__))");
      setTrace(JSON.parse(result));
    } catch (e) { setTrace({ steps: [], error: { type: "TracerError", message: String(e) }, source: code }); }
    setRunning(false);
  }, [py, code]);

  // auto-run once the runtime is ready and a problem is loaded
  useEffect(() => { if (status === "ready" && problem && !trace && !running) run(); }, [status, problem]); // eslint-disable-line

  const step = trace?.steps?.[idx];
  const structures = useMemo(() => {
    if (!step) return [];
    const out = [], locals = step.locals || {};
    const scopes = { ...locals };
    if (locals.self?.fields) Object.assign(scopes, locals.self.fields);
    const visited = (scopes.visited?.items || scopes.order?.items || []).map((x) => x.value);
    for (const [name, snap] of Object.entries(scopes)) {
      if (!snap || name === "self") continue;
      const el = renderValue(snap, { accent: name.includes("out") ? C.a2 : C.a1, visited });
      if (el) out.push({ name, el });
    }
    return out;
  }, [step]);

  /* ---------------- GENERAL VISUALIZER ---------------- */
  if (view === "general") {
    return <GeneralVisualizer onHome={() => setView("landing")} />;
  }

  /* ---------------- LANDING ---------------- */
  if (view === "landing") {
    const counts = CATS.map((c) => LIBRARY.filter((p) => p.category === c).length);
    return (
      <div className="min-h-screen font-sans" style={{ background: C.bg, color: C.text }}>
        <style>{baseCss}</style>
        <Nav onLibrary={() => setView("library")} onGeneral={() => setView("general")} />
        <div className="max-w-5xl mx-auto px-6 pt-16 pb-20">
          <div className="font-mono text-[11px] uppercase tracking-[0.3em] mb-5" style={{ color: C.a1 }}>execution, made visible</div>
          <h1 className="text-5xl md:text-6xl leading-[1.05] tracking-tight mb-6" style={{ color: C.ink, fontWeight: 600 }}>
            Watch your code<br />actually <span style={{ color: C.a1 }}>run</span>.
          </h1>
          <p className="text-lg max-w-xl leading-relaxed mb-8" style={{ color: C.dim }}>
            A library of classic data-structure problems, each with a full writeup — then watch the
            solution execute line by line in your browser, with every variable and pointer animated.
          </p>
          <div className="flex gap-3 mb-16">
            <button onClick={() => setView("library")} className="font-mono text-sm px-5 py-2.5 rounded-sm" style={{ background: C.a1, color: "#0a0d11", fontWeight: 600 }}>browse problems</button>
            <button onClick={() => setView("general")} className="font-mono text-sm px-5 py-2.5 rounded-sm" style={{ border: `1px solid ${C.border2}`, color: C.dim }}>paste your own code →</button>
          </div>
          <div className="grid grid-cols-2 md:grid-cols-5 gap-3">
            {CATS.map((t, i) => (
              <button key={t} onClick={() => { setActiveCat(t); setView("library"); }} className="rounded-md p-4 text-left transition-colors" style={{ background: C.panel, border: `1px solid ${C.line}` }}>
                <div className="h-1 w-8 rounded-full mb-3" style={{ background: CAT_ACCENT[t] }} />
                <div className="font-mono text-xs mb-1" style={{ color: C.ink }}>{t}</div>
                <div className="font-mono text-[10px]" style={{ color: C.faint }}>{counts[i]} problems</div>
              </button>
            ))}
          </div>
          <div className="mt-20 grid md:grid-cols-3 gap-5">
            {[["01", "Pick a problem", "Browse by structure. Each problem has a statement, hints, complexity, and the mistakes people actually make."],
              ["02", "Run the solution", "Real Python executes in-browser via Pyodide. A sys.settrace tracer records every line into a language-agnostic trace."],
              ["03", "See it move", "Arrays become boxes, trees become nodes, graphs light up their frontier. Step, replay, control speed."]].map(([n, t, d]) => (
              <div key={n}><div className="font-mono text-xs mb-2" style={{ color: C.a1 }}>{n}</div><div className="text-base mb-2" style={{ color: C.ink }}>{t}</div><div className="text-sm leading-relaxed" style={{ color: C.dim }}>{d}</div></div>
            ))}
          </div>
        </div>
        <Footer />
      </div>
    );
  }

  /* ---------------- LIBRARY ---------------- */
  if (view === "library") {
    const problems = LIBRARY.filter((p) => p.category === activeCat);
    return (
      <div className="min-h-screen font-sans" style={{ background: C.bg, color: C.text }}>
        <style>{baseCss}</style>
        <Nav onLibrary={() => setView("library")} onGeneral={() => setView("general")} onHome={() => setView("landing")} />
        <div className="max-w-6xl mx-auto px-5 py-6 grid md:grid-cols-[200px_1fr] gap-6">
          <aside className="flex md:flex-col gap-1.5 flex-wrap">
            <div className="font-mono text-[11px] uppercase tracking-[0.2em] mb-2 hidden md:block" style={{ color: C.dim }}>categories</div>
            {CATS.map((c) => {
              const active = c === activeCat, n = LIBRARY.filter((p) => p.category === c).length;
              return (
                <button key={c} onClick={() => setActiveCat(c)} className="text-left font-mono text-xs px-3 py-2 rounded-sm transition-colors flex items-center justify-between gap-2"
                  style={{ background: active ? C.panel : "transparent", border: `1px solid ${active ? CAT_ACCENT[c] + "66" : "transparent"}`, color: active ? C.ink : C.dim }}>
                  <span className="flex items-center gap-2"><span className="h-2 w-2 rounded-full" style={{ background: CAT_ACCENT[c] }} />{c}</span>
                  <span style={{ color: C.faint }}>{n}</span>
                </button>
              );
            })}
          </aside>
          <main>
            <h2 className="text-2xl mb-1 tracking-tight" style={{ color: C.ink }}>{activeCat}</h2>
            <p className="font-mono text-[11px] mb-5" style={{ color: C.faint }}>{problems.length} problems · click to open in the studio</p>
            <div className="grid sm:grid-cols-2 gap-3">
              {problems.map((p) => (
                <button key={p.title} onClick={() => openProblem(p)} className="text-left rounded-md p-4 transition-all hover:-translate-y-0.5"
                  style={{ background: C.panel, border: `1px solid ${C.line}` }}>
                  <div className="flex items-center justify-between mb-2">
                    <Pill color={DIFF_COLOR[p.difficulty]}>{p.difficulty}</Pill>
                    <span className="font-mono text-[10px]" style={{ color: CAT_ACCENT[p.category] }}>↗ open</span>
                  </div>
                  <div className="text-base mb-1.5" style={{ color: C.ink }}>{p.title}</div>
                  <div className="text-[13px] leading-relaxed line-clamp-3" style={{ color: C.dim }}>{p.statement}</div>
                  <div className="font-mono text-[10px] mt-3" style={{ color: C.faint }}>{p.complexity}</div>
                </button>
              ))}
            </div>
          </main>
        </div>
        <Footer />
      </div>
    );
  }

  /* ---------------- STUDIO ---------------- */
  return (
    <div className="min-h-screen font-sans" style={{ background: C.bg, color: C.text }}>
      <style>{baseCss}</style>
      <div className="max-w-7xl mx-auto px-5 py-4">
        <div className="flex items-center justify-between border-b pb-3 mb-4" style={{ borderColor: C.line }}>
          <div className="flex items-center gap-3">
            <button onClick={() => setView("library")} className="font-mono text-xs px-3 py-1.5 rounded-sm" style={{ border: `1px solid ${C.border2}`, color: C.dim }}>← library</button>
            <span className="text-sm" style={{ color: C.ink }}>{problem?.title}</span>
            {problem && <Pill color={DIFF_COLOR[problem.difficulty]}>{problem.difficulty}</Pill>}
          </div>
          <div className="font-mono text-[11px]" style={{ color: status === "ready" ? C.a4 : C.dim }}>
            {status === "loading" && "● loading python…"}{status === "ready" && "● python ready"}{status === "error" && "● runtime failed"}{status === "idle" && "○ idle"}
          </div>
        </div>

        <div className="grid lg:grid-cols-[1fr_1.1fr] gap-4">
          {/* left: writeup + editor */}
          <div className="flex flex-col gap-3">
            <div className="rounded-md overflow-hidden" style={{ background: C.panel, border: `1px solid ${C.line}` }}>
              <div className="flex border-b" style={{ borderColor: C.line }}>
                {["problem", "hints", "mistakes"].map((t) => (
                  <button key={t} onClick={() => setTab(t)} className="font-mono text-[11px] px-4 py-2.5 capitalize transition-colors"
                    style={{ color: tab === t ? C.ink : C.dim, borderBottom: `2px solid ${tab === t ? C.a1 : "transparent"}`, background: tab === t ? C.panel2 : "transparent" }}>{t}</button>
                ))}
                <div className="ml-auto font-mono text-[10px] px-4 py-2.5" style={{ color: C.faint }}>{problem?.complexity}</div>
              </div>
              <div className="p-4 text-[13.5px] leading-relaxed" style={{ color: C.text, minHeight: 96 }}>
                {tab === "problem" && <p className="m-0">{problem?.statement}</p>}
                {tab === "hints" && <ul className="m-0 pl-4 flex flex-col gap-2">{problem?.hints.map((h, i) => <li key={i} style={{ color: C.dim }}>{h}</li>)}</ul>}
                {tab === "mistakes" && <ul className="m-0 pl-4 flex flex-col gap-2">{problem?.mistakes.map((h, i) => <li key={i} style={{ color: C.dim }}>{h}</li>)}</ul>}
              </div>
            </div>

            <textarea value={code} onChange={(e) => setCode(e.target.value)} spellCheck={false}
              className="font-mono text-[12.5px] leading-[1.5] rounded-md p-3 resize-none"
              style={{ background: C.panel, border: `1px solid ${C.line}`, color: C.text, minHeight: 240, outline: "none" }} />
            <button onClick={run} disabled={status !== "ready" || running} className="font-mono text-sm py-2.5 rounded-md"
              style={{ background: status === "ready" ? C.a1 : C.border2, color: "#0a0d11", fontWeight: 600, opacity: running ? 0.6 : 1, cursor: status === "ready" ? "pointer" : "not-allowed" }}>
              {running ? "tracing…" : status === "ready" ? "▶ run & trace" : "loading runtime…"}
            </button>

            {trace && step && (
              <div className="rounded-md overflow-hidden" style={{ background: C.panel, border: `1px solid ${C.line}` }}>
                <div className="px-3 py-2 text-[11px] uppercase tracking-[0.2em] font-mono border-b" style={{ color: C.dim, borderColor: C.line }}>source · line {step.line}</div>
                <pre className="text-[12px] leading-[1.5] font-mono p-3 m-0 overflow-x-auto">
                  {code.split("\n").map((ln, i) => {
                    const active = i + 1 === step.line;
                    return (<div key={i} className="flex px-2 -mx-2 rounded-sm transition-colors duration-150" style={{ background: active ? `${C.a1}1a` : "transparent" }}>
                      <span className="w-7 text-right pr-3 select-none inline-block" style={{ color: active ? C.a1 : C.faint }}>{i + 1}</span>
                      <span style={{ color: active ? C.ink : C.dim }}>{ln || " "}</span></div>);
                  })}
                </pre>
              </div>
            )}
          </div>

          {/* right: visualization */}
          <div className="flex flex-col gap-3">
            {!trace && <div className="rounded-md flex items-center justify-center text-center p-10" style={{ background: C.panel, border: `1px dashed ${C.border2}`, minHeight: 300 }}>
              <div><div className="font-mono text-sm mb-2" style={{ color: C.dim }}>{status === "ready" ? "running…" : "loading python runtime…"}</div><div className="font-mono text-[11px]" style={{ color: C.faint }}>first load fetches Pyodide (~6MB)</div></div></div>}
            {trace?.error && <div className="rounded-md p-4 font-mono text-xs" style={{ background: C.panel, border: `1px solid ${C.a5}55`, color: C.a5 }}>{trace.error.type}: {trace.error.message}</div>}
            {trace && step && (<>
              <div className="rounded-md p-4" style={{ background: C.panel, border: `1px solid ${C.line}`, minHeight: 260 }}>
                <div className="text-[11px] uppercase tracking-[0.2em] font-mono mb-3" style={{ color: C.dim }}>data structures</div>
                <div className="flex flex-col gap-5">
                  {structures.length === 0 && <div className="font-mono text-[11px]" style={{ color: C.faint }}>no visualizable structure in scope at this step</div>}
                  {structures.map(({ name, el }) => (
                    <div key={name} className="flex flex-col gap-2">
                      <div className="font-mono text-[10px]" style={{ color: (step.changed?.includes(name) || (step.locals?.self && step.changed?.includes("self"))) ? C.a2 : C.dim }}>{name}</div>{el}</div>
                  ))}
                </div>
              </div>
              <div className="rounded-md p-4" style={{ background: C.panel, border: `1px solid ${C.a1}33` }}>
                <div className="text-[11px] uppercase tracking-[0.2em] font-mono mb-2" style={{ color: C.a1 }}>explanation</div>
                <p className="text-[13px] leading-relaxed m-0" style={{ color: C.text }}>{explain(step)}</p>
                {step.note && step.event !== "line" && <p className="font-mono text-[11px] mt-2 mb-0" style={{ color: C.dim }}>{step.note}</p>}
              </div>
              <div className="rounded-md p-3" style={{ background: C.panel, border: `1px solid ${C.line}` }}>
                <div className="text-[11px] uppercase tracking-[0.2em] font-mono mb-2" style={{ color: C.dim }}>variables · {step.function}()</div>
                <div className="flex flex-wrap gap-2">
                  {Object.entries(step.locals || {}).filter(([k]) => k !== "self" && !/^[A-Z]/.test(k)).map(([k, v]) => (
                    <div key={k} className="font-mono text-[11px] px-2 py-1 rounded-sm" style={{ background: C.panel2, border: `1px solid ${step.changed?.includes(k) ? C.a2 : C.border}` }}>
                      <span style={{ color: C.dim }}>{k}=</span><span style={{ color: step.changed?.includes(k) ? C.a2 : C.text }}>{fmt(v)}</span></div>
                  ))}
                </div>
              </div>
            </>)}
            {trace && trace.steps.length > 0 && (
              <div className="flex items-center gap-2 flex-wrap">
                <button onClick={() => { setIdx(0); setPlaying(false); }} className="ctrl">⏮</button>
                <button onClick={() => { setPlaying(false); setIdx((i) => Math.max(0, i - 1)); }} className="ctrl">◂ prev</button>
                <button onClick={() => setPlaying((p) => !p)} className="ctrl" style={{ background: C.a1, color: "#0a0d11", borderColor: C.a1 }}>{playing ? "❚❚" : "▶"}</button>
                <button onClick={() => { setPlaying(false); setIdx((i) => Math.min(trace.steps.length - 1, i + 1)); }} className="ctrl">next ▸</button>
                <button onClick={() => { setIdx(trace.steps.length - 1); setPlaying(false); }} className="ctrl">⏭</button>
                {[0.5, 1, 2, 4].map((s) => (<button key={s} onClick={() => setSpeed(s)} className="ctrl" style={speed === s ? { color: C.a1, borderColor: C.a1 } : {}}>{s}×</button>))}
                <span className="font-mono text-[11px] ml-1" style={{ color: C.faint }}>{idx}/{trace.steps.length - 1}</span>
                <input type="range" min={0} max={trace.steps.length - 1} value={idx} onChange={(e) => { setPlaying(false); setIdx(Number(e.target.value)); }} className="flex-1 min-w-[140px]" style={{ accentColor: C.a1 }} />
              </div>
            )}
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
}

function Nav({ onLibrary, onHome, onGeneral }) {
  return (
    <div className="max-w-5xl mx-auto px-6 py-5 flex items-center justify-between">
      <button onClick={onHome || onLibrary} className="font-mono text-sm" style={{ color: C.ink }}>codeviz <span style={{ color: C.a1 }}>·</span></button>
      <div className="flex items-center gap-2">
        {onGeneral && <button onClick={onGeneral} className="font-mono text-xs px-4 py-2 rounded-sm" style={{ border: `1px solid ${C.border2}`, color: C.dim }}>general visualizer</button>}
        <button onClick={onLibrary} className="font-mono text-xs px-4 py-2 rounded-sm" style={{ background: C.a1, color: "#0a0d11" }}>browse problems →</button>
      </div>
    </div>
  );
}
function Footer() {
  return <div className="max-w-7xl mx-auto px-6 py-8 font-mono text-[11px]" style={{ color: C.faint, borderTop: `1px solid ${C.line}` }}>codeviz · traces run locally in your browser, nothing is uploaded</div>;
}

const baseCss = `@media (prefers-reduced-motion: reduce){*{transition:none!important;animation:none!important}}
.ctrl{font-family:ui-monospace,monospace;font-size:11px;padding:6px 11px;border-radius:4px;background:#0e1116;color:#9aa6b3;border:1px solid #232b35;cursor:pointer;transition:all .15s}
.ctrl:hover{color:#eef3f8;border-color:#3a434f}
.line-clamp-3{display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
@keyframes popIn{from{opacity:0;transform:scale(.6)}to{opacity:1;transform:scale(1)}}`;
