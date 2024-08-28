def right(rows):
    for i in range(0,row+1):
        for j in range(0,i+1):
                print(chr(65+1*i),end=" ")
        print()
row=5
right(row)
