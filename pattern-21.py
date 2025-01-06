n=int(input())
count=1
for i in range(n):
    rows="*".join(str(count+j)for j in range(n-i))
    print(rows)
    count+=1
    
