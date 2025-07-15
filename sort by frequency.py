def frequencySort( s):
        order = ""
        frequency = {}
        for ch in s:
            if ch in frequency:
                frequency[ch] +=1
            else:
                frequency[ch]=1
        sorted_item = sorted(frequency.items(),key = lambda x:(-x[1],x[0]))
        for i,j in sorted_item:
            order += i*j
        return order

s = input("Enter a String:\n")
result = frequencySort(s)
print(result)

