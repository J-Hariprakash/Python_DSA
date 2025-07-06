def rotation_right(nums,k):
    l = len(nums)
    k %=l
    newArr = nums.copy()
    # OR newArr = [0]*l
    for i in range(l):
        newArr[(i+k)%l] = nums[i]
    for i in range(l):
        nums[i] = newArr[i]        
    return nums
size = int(input("Enter Required Size for an array: \n"))
arr = []
for i in range(size):
    elmts = int(input("Enter elements required: \n"))
    arr.append(elmts)
nums = sorted(arr)
k = int(input("Enter number of rotaton required of an array: \n"))         
result = rotation_right(nums,k)
print(result)