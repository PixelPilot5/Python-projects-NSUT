def expo(n,m):
    ans=1
    for i in range(m):
        ans=ans*n
    return ans

x=int(input("enter the number:"))
n=int(input("enter the power:"))
print(expo(x,n))