def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        spaces = 2 * (n - i)
        for k in range(spaces):
            print(" ", end=" ")
        for l in range(i, 0, -1):
            print(l, end=" ")
        
        print()

n = 4
print_pattern(n)
