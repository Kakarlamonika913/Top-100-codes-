T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    even_count = N // 2
    odd_count = N - even_count
    if X % 2 == 0:
        print(even_count - 1)
    else:
        print(odd_count - 1)
