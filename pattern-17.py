n=int(input())
count = 1
for i in range(n):
    row = "*".join(str(count + j) for j in range(n))
    print(row)
    count += 4
