for _ in range(int(input())):
    a,b,c,m=map(int,input().split())
    s1,s2,s3=abs(a-b),abs(a-c),abs(c-b)
    if s1<=m or s2<=m or s3<=m:
        print('YES')
    else:
        print('NO')
