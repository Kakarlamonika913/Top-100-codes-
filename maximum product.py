# cook your dish here
for _ in range(int(input())):
    d,x,y,z=map(int, input().split())
    
    if (7*x) >= ((d*y) + (7-d)*z):
        print(7*x) 
    else:
        print((d*y) + (7-d)*z)
        
