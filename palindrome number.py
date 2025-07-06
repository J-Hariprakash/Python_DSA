def isPalindrome(x):
        temp = x
        rev =""
        if x >=0:
          s = str(x)
          for i in range(len(s)-1,-1,-1):
              rev+=s[i]
          r = int(rev)
          if r == temp:
            return True
        return False
x = int(input("Enter a number : \n"))
result = isPalindrome(x)
print(result)