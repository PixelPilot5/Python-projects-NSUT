def revstr(s):
    n=len(s)
    newstr=""
    for i in range(1,n+1):
        newstr=newstr+s[-i]

    return newstr

s=input("enter the string:")
print("reversed string=",revstr(s))