def last_non_zero_digit(n):
    result = 1
    for i in range(1, n + 1):
        result *= 1
        while result % 10 == 0:
            result //= 10
        result %= 10  # Keep only the last digit
    return result
n = int(input("Enter a number: "))
print(f"The last non-zero digit of {n}! is {last_non_zero_digit(n)}")
