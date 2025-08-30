def revstr(s):
    n=len(s)
    newstr=""
    for i in range(1,n+1):
        newstr=newstr+s[-i]

    return newstr==s

s=input("enter the string:")
s=s.lower()
# print("reversed string=",revstr(s))
if(revstr(s)):print("Yes it is a palindrome")
else:print("no it is not a palindrome")