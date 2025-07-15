unit = int(input("Enter unit:\n"))
sum = 0
if unit <= 50 :
    print(unit*0.5)
elif unit>50 and unit<=150:
    print(unit*0.75)
elif unit>150 and unit<=250:
    print(unit*1.20)
elif unit >250 and unit<=350:
    print(unit*1.5)
else:
    prct = (unit*20)//100
    amt = unit*1.75
    print(prct+amt)