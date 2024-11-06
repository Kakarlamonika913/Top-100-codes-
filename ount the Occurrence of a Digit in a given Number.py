def count_digits(n,d):
    cnt=0
    while n>0:
        if n%10==d:
            cnt=cnt+1
        n=n//10
    return cnt
d=int(input())
n=int(input())
print(count_digits(n,d))
