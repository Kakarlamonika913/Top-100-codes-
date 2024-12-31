n=int(input())
count=1
for i in range(n):
    rows="*".join(str(count+j)for j in range(i+1))
    print(rows)
    count+=1
