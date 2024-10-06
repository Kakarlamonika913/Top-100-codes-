t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    c,s = 0,0
    for e in l:
        s+=e
        if s > k: break 
        c+=1
    print(c)
