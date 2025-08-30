def isprime(n):
    if n==1: return False
    for i in range(2,n):
        if(n%i==0):
            return False
        
    return True
    
a=int(input("enter the nubmer:"))
if(isprime(a)):print("it is prime")
else:print("not prime")