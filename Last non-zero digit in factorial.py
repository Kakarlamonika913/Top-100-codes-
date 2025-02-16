def last_nonzero_digit(n):
    if n == 0:
        return 1
    last_digits = [1, 1, 2, 6, 4, 2, 2, 4, 8, 6]
    result = 1
    while n > 0:
        if (n // 10) % 2:  # If quotient when divided by 10 is odd
            result *= 4
        result *= last_digits[n % 10]
        result %= 10  
        n //= 5
    return result
n = 100
print(last_nonzero_digit(n)) 
