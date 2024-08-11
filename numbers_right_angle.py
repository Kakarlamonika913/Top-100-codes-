def right(n):
        for i in range(1,rows+1):
            for j in range(1,i+1):
                print(j,end=" ")
            print()
rows=5
right(rows)
