def pattern(rows):
    for i in range(rows,0,-1):
        for j in range(i):
             print(chr(65 +j), end=" ")
        print()  

rows = 4
pattern(rows)
