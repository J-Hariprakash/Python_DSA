def palindromes(n,rev):
    if n==0:
        print(rev)
        return
    rem=n%10
    rev=rev*10+rev
    palindromes(n//10,rev)
palindromes(589,rev=0)
