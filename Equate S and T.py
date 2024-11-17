 
    

# cook your dish here
for _ in range(int(input())):
    n,m = map(int,input().split())
    s = input()
    t = input()
    
    # print(s)
    # print(s[:len(s)-1])
    
    while s and t:
        # print(f'{s=} {t=}')
        if s[-1] == t[-1]:
            s = s[:len(s)-1]
            t = t[:len(t)-1]
            
        elif s[-1]=='a':
            s+='b'
        else:
            t+='b'
    # print(f'{s=} {t=}')
            
    if s == t:
        print('YES')
    else:
        print('NO')
        # print(s,t)
    
    
    
    
    
    
    
    
    
