for i in range(int(input())):
    a,c,g = map(int,input().split())
    if(c*g<a):
        print('yes')
    else: print('no')
