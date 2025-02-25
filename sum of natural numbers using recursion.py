def natural_number(n):
    sum=0
    for i in range(n):
        sum=sum+i
    return sum
n=int(input())
print(natural_number(n))
