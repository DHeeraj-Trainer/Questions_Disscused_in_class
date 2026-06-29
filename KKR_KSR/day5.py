# word=" Hello      "
# print(word,len(word),len(word.strip()),len(word.lstrip()),len(word.rstrip()))
# word=input("word: ").strip().split(',')
# print((word),type(word[0]))
# res=[]
# for i in word:
#     res.append(int(i))
# print(res,type(res[0]))
# res=list(map(int,input("word: ").strip().split(',')))
# print(res,type(res[0]))


# s=input("enter the numbers sep by space: ").split()#123 45 67 89
# res=[]
# for i in s:
#     sum=0
#     for j in i:
#         sum+=int(j)
#     res.append(str(sum))
# print(" ".join(res))
# inpu_str=input("enter the numbers sep by space: ")
# def sum_split(inpu_str):
#     return " ".join(str(sum(map(int,num))) for num in inpu_str.split())
# print(sum_split(inpu_str))
def sum_split(inpu_str):
    res=''
    for num in inpu_str.split():
        res+=str(sum(map(int,num))) +" "
    return res
# print(sum_split(inpu_str))

# print(str(sum(list(map(int,"123")))))


# s=input("enter str:")
# nr=int(input("no of rotations:"))
# n=nr%len(s)
# print(s[n:]+s[:n])



# word=input("enter:") #abbcdeaa
# for i in word:
#     if word.count(i)==1:
#         print(i)
#         break


