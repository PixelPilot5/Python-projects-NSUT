def fibo(n):
    if(n==1):return 0
    if(n==2):return 1
    return fibo(n-1)+fibo(n-2)

a=int(input("enter the number:"))
for i in range(1,a+1):
    print(fibo(i),end=" ")
