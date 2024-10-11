t = int(input())  
for _ in range(t):
    N = int(input())
    area = 0  
    for l in range(1, N // 2):
        b = (N - 2 * l) // 2
        if b > 0:
            area = max(area, l * b)
    print(area)
