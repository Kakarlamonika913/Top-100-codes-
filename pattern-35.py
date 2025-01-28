n = 4
for i in range(1, n + 1):
    print('*'.join([str(i)] * i))
for i in range(n, 0, -1):
    print('*'.join([str(i)] * i))
