rows = 3  

for i in range(rows):
  
    for space in range(rows - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print(4 - j, end=" ")
    print()
