A coding contest has N submissions.
Each submission contains:
Username ProblemID Score
Rules:
"""
A user's score for a problem is the highest score they achieved on that problem.
Total score = sum of highest scores across all problems.
Rank users by:
Higher total score.
Fewer solved problems (score > 0) is ranked lower.
Alphabetical order if still tied.
Print the leaderboard.
Input
8
Rahul A 80
Rahul A 100
Anita A 90
Rahul B 70
Anita B 100
Raj A 100
Raj B 50
Raj B 80
Output
Anita 190
Rahul 170
Raj 180

"""
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum=float("-inf")
	for i in range(len(nums)-k+1):
		curr_sum=sum(nums[i:i+k])
		max_sum=max(max_sum,curr_sum)
	return max_sum/k

nums=[1,2,4,5,8,7,9,6] n=len=8
k=4
1245 nums[:4]  [0:k+0]
2458 nums[1:5] [1:k+1]
4587 nums[2:6]
5879 nums[3:7]
8796 nums[4:8]  [4:k+4]  [i:k+i]
i=0,1,2,3,4   len(nums)-k+1             
for i in range(len(nums)-k+1):
	print(nums[i:i+k])


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # max_sum=float("-inf")
        # for i in range(len(nums)-k+1):
        #     curr_sum=sum(nums[i:i+k])
        #     max_sum=max(max_sum,curr_sum)
        # return max_sum/k
        window_sum=sum(nums[:k])
        max_sum=window_sum
        for i in range(k,len(nums)):
            window_sum+=nums[i]
            window_sum-=nums[i-k]
            max_sum=max(max_sum,window_sum)
        return max_sum/k
"""
"""
abcabcbb
a   l=1  m=1
ab l=2  m=2
abc l=3 m=3
bca l=3 m=3
bcab--cab l=3 m=3  
cabc----abc l=3 m=3
abcb-----bcb------cb len=2  m=3
cbb----bb-----b=1  m=3

index  char dup? action  window  l
0      a   no    add a    a     1
1      b    no   add b    ab    2
2       c    no  add c    abc    3
3      a     yes remove a  bc   2
       a     yes move left bca   3
4      b     yes  remove b  cab   3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
	seen=set()
	max_len=0
	for right in range(len(s)):
		while s[right] in seen:
			seen.remove(s[left])
			left+=1
		seen.add(s[right])
		max_len=max(max_len,right-left+1)
	return max_len
abcabcbb  len=8
left  right  seen   max_len
0              {}     0
0      0     {a}     (0,0-0+1)=1
0      1     {a,b}    (1,1-0+1)=2
0      2    {a,b,c}   (2,2-0+1)=3
0->1   3     {b,c}-->{b,c,a}   (3,3-1+1)=3
1->2   4     {b,c,a}>>{c,a}>>{c,a,b}(3,4-2+1)=3
2->3   5    {c,a,b}>>{ab}>>{abc}   (3,5-3+1)=3
3->4   6    {abc}>{bc}>>{bcb}   (3,6-4+1)=3
4->5   7    {bcb}>{cb}>>cbb   (3,7-5+1)=3


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        seen=set()
        max_len=0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            max_len=max(max_len,right-left+1)
        return max_len

"""

