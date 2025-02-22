def rotate_array(arr, k):
    if not arr: 
        return arr
    k %= len(arr)  
    return arr[-k:] + arr[:-k]
arr = [1, 2, 3, 4, 5]
k = 2
print(rotate_array(arr, k))  # Output: [4, 5, 1, 2, 3]
