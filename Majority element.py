def  majority(nums):
    frequent = {}
    for elmt in nums:
        if elmt not in frequent:
            frequent[elmt] = 1
        else:
            frequent[elmt]+=1         
    for index,num in frequent.items():
        if num > (len(nums)/2):
            return index

size = int(input("Enter Required Size for an array: \n"))
nums = []
for i in range(size):
    elmts = int(input("Enter elements required: \n"))
    nums.append(elmts)     
result = majority(nums)
print(result)