for _ in range(int(input())):
    d,x,y,z=map(int, input().split())
    
    if (7*x) >= ((d*y) + (7-d)*z):
        print(7*x) #if both are works are equal he should choose this method because he does max work without getting tired.
        
    else:
        print((d*y) + (7-d)*z)
        
