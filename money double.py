for _ in range(int(input())):
    a,b=map(int,input().split())
    for i in range(b):
        if a+1000>(2*a):
            a=(a+1000)
        else:
            a=(2*a)
    print(a)
