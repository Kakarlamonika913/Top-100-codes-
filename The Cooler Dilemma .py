# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x>=y:
        print('0')
    elif x<y and y%x!=0:
        print(y//x)
    else:
        print((y//x)-1)
