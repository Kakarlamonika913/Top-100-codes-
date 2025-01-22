rows = 8
for i in range(1, rows + 1):
    if i <= 4:
        for _ in range(i):
            print(i, end="*")
        print("\b") 
    else:
        j = rows - i + 1
        for _ in range(j):
            print(j, end="*")
        print("\b")  # Removes the trailing '*'
