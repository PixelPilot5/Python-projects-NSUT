def isprime(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if(n%i==0):return False

    return True

a=int(input("enter the lower range:"))
b=int(input("enter the higher range:"))
for i in range(a,b+1):
    if(isprime(i)):
        print(i)