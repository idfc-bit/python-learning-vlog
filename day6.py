#list in python 
india = ["karnataka", "kerala","tamil nadu","andra pradesh"]
print(india)
print(india.pop())
india.append("north india")
print(india)




virat = ["goat","king", "run machine", "anushka pati"]
virat.append("saviour of indian team")
print(virat)
l = virat.pop()
print(l)                                                               #modifying strings
virat.insert(2,"centurian") 
print(virat)
virat.remove("anushka pati")
print(virat)

print(virat[::3])
print(virat[2:])                                                                        #[start:end:skip]
                                         

numbers = [1,2,4,5,3,5,6,7,8]
sorted(numbers)
print(numbers)
print(numbers)
print(numbers[::3])
print(numbers[::2])
rev = numbers.reverse
print(rev)