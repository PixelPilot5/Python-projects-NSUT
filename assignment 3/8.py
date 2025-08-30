def hcf(a,b):
    if(a%b==0):return b

    return hcf(b,a%b)

a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
print(hcf(a,b))