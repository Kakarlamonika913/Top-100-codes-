import math
for i in range(int(input())):
    x,y = map(int,input().split())
    dish = math.floor(x/2)
    if (y>dish):
        print(dish)
    else:
        print(y)
