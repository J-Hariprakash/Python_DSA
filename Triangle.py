l1 = int(input("enter a lenght:\n"))
l2 = int(input("enter a lenght:\n"))
l3 = int(input("enter a lenght:\n"))

if l1 == l2 and l2 == l3:
    print("Equilateral")
elif l1 == l2 or l2 == l3:
    print("isoscles")
else:
    print("Scalene")