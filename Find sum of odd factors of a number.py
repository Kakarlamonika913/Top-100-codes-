def sum_of_odd_factors(n):
    total = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i % 2 == 1: 
                total += i
            if (n // i) % 2 == 1 and (n // i) != i:  
                total += n // i
    return total
n = 18  
print(sum_of_odd_factors(n))  # Output: 13
