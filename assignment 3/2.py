import math
rows=int(input("enter number of rows"))
for i in range(0,rows):
    print(' ' * (rows - i), end='')
    for j in range(0,i+1):
        print(math.comb(i,j),end=" ")
    print("\n")