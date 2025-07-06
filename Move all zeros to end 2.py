def Move_all(arr):
  j = 0
  for i in range(len(arr)):
     if arr[i] != 0:
        arr[j] = arr[i]
        j+=1
  n = len(arr) - j     
  arr[j:] = [0]*n
  return arr            
    
size = int(input("Enter Required Size for an array: \n"))
arr = []
for i in range(size):
    elmts = int(input("Enter elements required: \n"))
    arr.append(elmts)     
result = Move_all(arr)
print(result)
