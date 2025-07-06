def TwoSum(Size,Target):
    flag = 0
    for i in range(0,Size-1):
       for j in range(i+1,Size):
         if nums[i] + nums[j] == Target:
            flag = 1
            print("Target found at" "[",i,",",j,"]")
    if flag != 1:
     print("Target Not found")
Size = int(input("Enter an Size of list: \n"))
nums = []
for Elements in range(Size):
    Elmnt = int(input("Enter Values Required in an Array: \n"))
    nums.append(Elmnt)
Target = int(input("Enter an Targetted Value: \n"))
TwoSum(Size,Target)

   

   
       
          
 



