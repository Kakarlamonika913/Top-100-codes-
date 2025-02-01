def count_decodings(digits):
    if not digits or digits[0] == '0': return 0
    a, b = 1, 1
    for i in range(1, len(digits)):
        temp = b if digits[i] != '0' else 0
        if 10 <= int(digits[i-1:i+1]) <= 26:
            temp += a
        a, b = b, temp
    return b
digits = "226"
print(count_decodings(digits))
