def singleNumber(nums):
    nums = sorted(nums)
    i,l = 1,len(nums)
    while i<l:
        if nums[i-1]!=nums[i]:
            if i == 1:
                return nums[i-1]
            elif nums[i] == nums[l-1] or nums[i]!=nums[i+1]:  
                return nums[i]
            else:
                i+=1 
        else:
            i+=1
    else:
        return nums[l-1]      
            
size = int(input("Enter Required Size for an numsay: \n"))
nums = []
for i in range(size):
    elmts = int(input("Enter elements required: \n"))
    nums.append(elmts)     
result = singleNumber(nums)
print(result)