import random
while(True):
    a=random.randint(1,6)
    b=random.randint(1,6)
    print("first dice=",a,"second dice=",b)
    c=int(input("1 for continue, 0 for end"))
    if(c==0):break