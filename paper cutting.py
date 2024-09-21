T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    number_of_squares = (N//K) ** 2
    print(number_of_squares)
