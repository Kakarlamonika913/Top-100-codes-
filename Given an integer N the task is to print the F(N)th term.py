def fibonacci(N):
    if N < 0:
        return "Invalid input. N must be a non-negative integer."
    elif N == 0:
        return 0
    elif N == 1:
        return 1
    a, b = 0, 1  
    for _ in range(2, N + 1):
        a, b = b, a + b 
    return b
N = int(input("Enter a number: "))
print(f"F({N}) =", fibonacci(N))
