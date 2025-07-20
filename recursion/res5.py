def res5(x):
    if x==11:
        return "biscuit"
    print(x) 
    y = res5(x+1)
    print(x)
    return y
print(res5(1))
