def right(n):
    n=1
    for i in range(1,rows+1):
        for j in range(i):
            print(n,end=" ")
            n=n+1
        print()
rows=5
right(size)
