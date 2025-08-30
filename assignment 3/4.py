def sumofdigits(n):
    sum=0
    while(n>0):
        # sum=sum*10
        sum=sum+n%10
        n=n//10

    return sum

a=int(input("enter the number:"))
print(sumofdigits(a))