def tower(n,s,h,d):
    if n==1:
        print("move",n,"from",s,"to",d)
        return 
    tower(n-1,s,d,h)
    print("move",n,"from",s,"to",d)
    tower(n-1,h,s,d)
tower(3,"source","helper","destination")