def even_odd_divisors
    even_count=0
    odd_count=0
    for i in range(1,N+1):
        if N%i==0:
            if i%2==0:
                even_count+=1
            else:
                odd_count+=1
    if even_count>odd_count:
        return 1
    elif even_count==odd_count:
        return 0
    else:
        return -1

T=int(input())
for _in range(T):
    N=int(input())
    print(even_odd_divisors(N))
