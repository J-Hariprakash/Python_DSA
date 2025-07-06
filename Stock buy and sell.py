def stock(nums):
    l,max_profit,net =len(nums),0,0
    for i in range(0,l-1):
        for j in range(i+1,l):
            net = nums[j]-nums[i] 
            if max_profit < net :
                max_profit = net 
    return max_profit
size = int(input("Enter Required Size for an numsay: \n"))
nums = []
for i in range(size):
    elmts = int(input("Enter elements required: \n"))
    nums.append(elmts)     
result = stock(nums)
print("maximum profit :",result)