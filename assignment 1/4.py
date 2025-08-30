import math
a=int(input("enter the number:"))
isprime=1
if a<2:
    isprime=0

else:
    for i in range(2,a):
        if a%i==0 :
            isprime=0
            break

if isprime:
    print("YES")
else:
    print("NO")