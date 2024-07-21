def rearrange_alternating(arr):
    n = len(arr)
    i, j = 0, 1
    def swap(x, y):
        arr[x], arr[y] = arr[y], arr[x]
    for k in range(n):
        if arr[k] < 0 and k % 2 == 1:
            while j < n and arr[j] < 0:
                j += 2
            if j < n:
                swap(k, j)
        elif arr[k] >= 0 and k % 2 == 0:
            while i < n and arr[i] >= 0:
                i += 2
            if i < n:
                swap(k, i)
    pos, neg = 0, 1
    while pos < n and neg < n:
        if arr[pos] < 0 and arr[neg] >= 0:
            swap(pos, neg)
        pos += 2
        neg += 2

    return arr
arr = [1, 2, 3, -4, -1, 4]
rearranged_arr = rearrange_alternating(arr)
print(rearranged_arr)
