# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    while n>0:
        mod = n%2
        count += mod
        n //= 2
    if count%2==0:
        print('even')
    else:
        print('odd')
