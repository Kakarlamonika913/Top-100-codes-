def print_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print(chr(69 - j), end=" ")
        print()  

rows = 5
print_pattern(rows)