Str = input("Enter a String : \n")
Reveresd_word = ""
for i in range(len(Str)-1,-1,-1):
    Reveresd_word+= Str[i]
print(Reveresd_word)
#using built in function    
print("".join(reversed(Str)))
   