def merge_sort(arr,low,high):   
    if low<high:    
        mid = (low+high)//2 
        merge_sort(arr,low,mid)
        merge_sort(arr,mid+1,high)
        merge(arr,low,mid,high)
def merge(arr,low,mid,high):
    left = arr[low:mid+1]
    right = arr[mid+1:high+1]
    i,j,k = 0,0,low
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1 
        k+=1  
    while i<len(left):
        arr[k] = left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k] = right[j]
        j+=1
        k+=1

size = int(input("Enter Required Size for an array: \n"))
arr = []
for i in range(size):
    elmts = int(input("Enter elements required: \n"))
    arr.append(elmts)     
merge_sort(arr,0,len(arr)-1) 
print()
