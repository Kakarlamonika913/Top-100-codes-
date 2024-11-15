for _ in range(int(input())):
    n, x = map(int, input().split())
    #count = 0
    if x % 2 == 0:
        print(n//2-1)
        
    elif x % 2 != 0 and n % 2 != 0:
        print(n//2)
        
    else:
        print(n//2 - 1)
    
