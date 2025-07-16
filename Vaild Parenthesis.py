def Valid(s):
        stack =[]
        paranthesis = {')':'(','}':'{',']':'['}
        for ch in s:
            if ch not in paranthesis:
                stack.append(ch) 
            else:
                if stack:
                   top = stack.pop()
                   if paranthesis[ch]!=top:
                       return False
                else:
                    return False 
        return not stack 
s = input("Enter a paranthesis: \n")
result = Valid(s)
print(result)          