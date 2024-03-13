t=int(input())
for i in range(t):
    x=int(input())
    a=x*0.2
    b=int(100/a)
    c=int(a*b)
    
    if c>=100:
        print(b)
    else:
        print(b+1)
    
