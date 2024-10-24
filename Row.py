# cook your dish here

for i in range(int(input())):

    n,x=map(int,input().split())

    l=list(map(int,input().split()))

    res=(n*x)-(sum(l))

    if(res<0):

        print(0)

    else:

        print(res)
