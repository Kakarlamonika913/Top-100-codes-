arr = list(map(int, input().split()))
print([num for num in arr if arr.count(num) == 1])
