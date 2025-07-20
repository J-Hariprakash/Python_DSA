def res3(x):
    if x==11:
        return
    print(x) 
    res3(x+1)
    print(x)
res3(1)
