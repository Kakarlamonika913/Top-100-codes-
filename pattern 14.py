def print_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print(chr(65 + j), end=" ")
        print()  

rows = 4
print_pattern(rows)
