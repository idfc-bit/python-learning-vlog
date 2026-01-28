a = float(input("enter the temperature"))

if a>=40:
    print("heat alert")
elif a>=25 and a<40:
    print("warm water")
elif a>=10 and a<25:
    print("cool water")
else:
    print("cold water")