def common(words):
    d,freq,ans={},{},""
    for word in words:
        for ch in word:
            if ch in d:
                d[ch]+=1
            else:
                d[ch]=1
    for key,value in d.items():
        if value%len(words)==0:
            value//=len(words)
            freq[key]=value
    ans=""
    for key,value in freq.items():
        ans+=key*value
    return list(ans)
    
#words = list(map(str,input("Enter words:\n").split(",")))
words = ["cool","lock","cook"]
print(common(words))




