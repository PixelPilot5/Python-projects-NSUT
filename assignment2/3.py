import random
while(1):
    a=random.randint(1,10)
    correct=0
    i=0
    while i<4:
        b=int(input("enter your guess:"))
        if(b==-1):
            print("the number is",a)
            # i=i-1
            continue
        if(b==a):
            correct=1
            break
        elif b<a:
            print("guess a higher number")
            i=i+1

        else:
            print("enter a lower number:")
            i=i+1

        if  abs(a-b)==1:
            print("you are very close to the number")
    if(correct):
        print("you guessed the number correct that was",a)

    else:
        print("sorry you lost and the number was",a)


    playagain=int(input("do you want to play again? 0 for no , 1 for yes"))
    if(playagain==0):
        break
