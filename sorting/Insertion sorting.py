def Insertion_Sort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j = i-1
        while j>=0 and arr[j]>temp:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = temp
    return arr        

size = int(input("Enter a size of array: \n"))
arr =[]
for i in range(size):
    elemts = int(input("Enter a required elemkents: \n"))
    arr.append(elemts)
result = Insertion_Sort(arr)
print(result)    