x = 10
x += 10
print(x)       #if u give fucking values together this is wt fucking happen (it'll take previous value as operand )
x -= 20
print(x)
x *= 100
print(x)

a = 10
b = 20
a /= b
print(a)


#from now on fucking logical operators
a = 19
b = 20
print(a>b and b>a)       #and operator ( its true when both are true)
print(b>a and b>a )



a = 1
b = 2
print(a > b or b>a)
print( b>=a or a>b )     # or operator ( its false when both are false )




a = 19
b = 18
print(not(b<a))           # not operator ( its fucking opposite)
print(not(a<b))

#comparison operator(you can use it on all the operators)
print(not(a>b and b<a))




# from now on membership operator
chethan = "the goat"
likhith = "sangabulla"
print( "goat" in chethan )
print("goat" in likhith )
print(" sangabulla " not in likhith )          #string
print("sangabulla" in chethan )
  

classes = [1,2,3,4,5,6,7,8,9,10]
print("1,2,3,4,5" in classes)  
print("1,3,5" in classes)                 #list



# tupples
a = ("shata", "luvda","gandu")
#set
abs= {1,2,3,4,5}
