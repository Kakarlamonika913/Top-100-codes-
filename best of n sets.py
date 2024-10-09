for i in range(int(input())):
    x,y=map(int,input().split())
    print(x+y+(abs(x-y)-1))
