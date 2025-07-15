def anagram(s,t):
    Sort1 = "".join(sorted(Str1))
    Sort2 = "".join(sorted(Str2))
    if Sort1 == Sort2:
     return True
    else:
      return False
Str1 = input("enter a  String one :\n")
Str2 = input("enter a  String two :\n")
result = anagram(Str1,Str2)
print(result)   
