for  _ in range(int(input())):
    n=int(input())
    if(n<1500):
        print(n+0.1*n+0.9*n)
    else:
        print(n+500+n*0.98)
