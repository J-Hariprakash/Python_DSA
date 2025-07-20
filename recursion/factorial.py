# def facts(x):
#     if x==1:
#         return 1
#     return x*facts(x-1)
# print(facts(6))


# def fact1(x,i,fact):
#     if i==x+1:
#         print(fact)
#        return 
#     fact*=i
#     fact1(x,i+1,fact)
# allfact1(5,1,1)


def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+fibo(n-2)
print(fibo(10))






 