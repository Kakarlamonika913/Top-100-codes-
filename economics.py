T = int(input())
for t in range(T):
    n = int(input()) # the input has no use in out code
    s = list(map(int, input().split()))
    d = list(map(int, input().split()))
    count = 0
    for (i,j) in zip(s,d): # I used zip func for pairing. we can use value n also
        if i == j:
            count += 1
    print(count)
