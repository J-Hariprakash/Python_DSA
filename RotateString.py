def rotateString( s, goal):
        if len(s) == len(goal) and goal in (s+s):
          return True 
        else:
          return False
Str1 = input("enter a  String one :\n")
Str2 = input("enter a  String two :\n")
result = rotateString(Str1,Str2)
print(result)   