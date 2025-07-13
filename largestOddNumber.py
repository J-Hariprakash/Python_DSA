def largestOddNumber(num):
        l = len(num) - 1

        while l >= 0:
            x = int(num[l])
            if x % 2 == 1:
                return num[:l+1]
            l -= 1
        return ""
        
num = input("enter numbers:\n")
result = largestOddNumber(num)
print(result)