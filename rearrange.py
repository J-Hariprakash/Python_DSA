def rearrange(nums):
    j,k = 0,0
    l = len(nums)
    arr = nums.copy()
    for i in range(0,l):
        if i%2 == 0 or i == 0:
            while  j < l:
                if arr[j] > 0 :
                    nums[i] = arr[j]
                    j+=1
                    break
                else:
                    j+=1
        else:
             while  k < l:
                if arr[k] < 0 :
                    nums[i] = arr[k]
                    k+=1
                    break
                else:
                    k+=1
    return nums
size = int(input("Enter Required Size for an array: \n"))
nums = []
for i in range(size):
    elmts = int(input("Enter elements required: \n"))
    nums.append(elmts)     
result = rearrange(nums)
print(result)