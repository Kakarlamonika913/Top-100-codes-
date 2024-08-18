def diamond(n):
    for i in range(n):
        for j in range(0,n-i-1):
            print(" ",end=" ")
        for j in range(0,2*i+1):
            print("*" ,end=" ")
        print()
    for i in range(n):
        for j in range(i):
                print(" ",end=" ")
        for j in range(2*(n-i)-1):
            print("*",end=" ")
        print()
size=5
diamond(size)
