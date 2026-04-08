expression=input("enter: ")
x,y,z=expression.split(" ")
x=int(x)
z=int(z)
if y=="+":
    print(round(float(x+z),1))
elif y=="-":
    print(round(float(x-z),1))
elif y=="*":
    print(round(float(x*z),1))
elif y=="/" and z!=0:
    print(round((x/z),1))
else:
 print("invalid")