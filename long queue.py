for t in range(int(input())):
    n=int(input());
    a=list(map(int,input().split()));
    while(n):
        n-=1
        if a[n-1]>a[-1]/2:print(n+1);break;
