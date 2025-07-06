def frequency(arr):
    frequent = {}
    for elmt in arr:
        if elmt not in frequent:
            frequent[elmt] = 1
        else:
            frequent[elmt]+=1
    return frequent        
size = int(input("Enter Required Size for an array: \n"))
arr = []
for i in range(size):

    
    elmts = int(input("Enter elements required: \n")) 
    arr.append(elmts)     
result = frequency(arr) 
print(result)  