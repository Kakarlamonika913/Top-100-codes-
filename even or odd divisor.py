# cook your dish here
T = int(input())
for _ in range(T):
    N = int(input())
    f_N = 0 
    g_N = 0 
    
    for i in range(1, N + 1):
        if N % i == 0: 
            if i % 2 == 0:
                f_N += 1
            else: 
                g_N += 1
    
    if f_N > g_N:
        print(1)
    elif f_N == g_N:
        print(0)
    else:
        print(-1)
