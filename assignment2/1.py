a=int(input("enter the number:"))
fact=1;
if a<0 :
    print("invalid input")
else:
    for i in range(1,a+1):
        fact=fact*i

    print(fact)