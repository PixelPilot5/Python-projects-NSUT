import math
print("in ax2+bx+c")
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
disc=b*b-4*a*c
if disc<0:
    print("real roots not possible")
else:
    root1= (-b + math.sqrt(disc))/2.0*a
    root2= (-b - math.sqrt(disc))/2.0*a
    print("root1=",root1," root2=",root2)