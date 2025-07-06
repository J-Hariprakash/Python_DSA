def TwoSum(nums,Target):
    length =  len(nums)
    i,j = 0,1
    while(i < length-1):
        if j < length:
           if nums[i]+nums[j]!=Target:
              j+=1
           else:
              return [i,j]
        else:
            i+=1
            j = i+1
Size = int(input("Enter an Size of list: \n"))
nums = []
for Elements in range(Size):
    Elmnt = int(input("Enter Values Required in an Array: \n"))
    nums.append(Elmnt)
Target = int(input("Enter an Targetted Value: \n"))
result = TwoSum(nums,Target)
print(result)