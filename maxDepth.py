def maxDepth(s):
    count,max_count =0,0
    for ch in s:
        if ch=='(':
            count+=1
            max_count = max(max_count,count)
        elif ch==')':
            count-=1
    return max_count
s = input("Enter a paranthesis: \n")
result = maxDepth(s)
print(result) 