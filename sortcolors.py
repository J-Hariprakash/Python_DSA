def sortcolor(nums):
    hashs = {}
    for elmt in nums: 
        if elmt not in hashs:
            hashs[elmt] = 1
        else:
            hashs[elmt]+=1
    red = hashs.get(0, 0)
    white = hashs.get(1, 0)
    blue = hashs.get(2, 0)
    nums[:red] = [0]*red
    nums[red:red+white] = [1]*white
    nums[red+white:] = [2]*blue
size = int(input("Enter Required Size for an array: \n"))
nums = [] 
for i in range(size):
    elmts = int(input("Enter elements required: \n"))
    nums.append(elmts)
sortcolor(nums)
print(nums)