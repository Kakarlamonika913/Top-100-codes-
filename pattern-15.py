n=int(input())
for i in range(n):
    for j in range(i+1):
        print(i*1+1,end="")
    print()
for i in range(n):
    for j in range(n-i):
        print(i*1+1,end="")
    print()
