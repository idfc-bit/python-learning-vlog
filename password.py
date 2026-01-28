username = input("enter the name")
b = int(input("enter the pin"))

if username=="admin":
    if b==1234:
        print("password and username is correct")
    else:
        print("given data is incorrect")
else:
    print("user not found")