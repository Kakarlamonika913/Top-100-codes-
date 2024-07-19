def three_way_partition(arr, low_val, high_val):
    start = 0
    end = len(arr) - 1
    i = 0
    
    while i <= end:
        if arr[i] < low_val:
            arr[i], arr[start] = arr[start], arr[i]
            start += 1
            i += 1
        elif arr[i] > high_val:
            arr[i], arr[end] = arr[end], arr[i]
            end -= 1
        else:
            i += 1
    return arr
arr = [1, 4, 5, 3, 2, 7, 8, 6, 2, 3, 3]
low_val = 3
high_val = 5
print("Original array:", arr)
partitioned_arr = three_way_partition(arr, low_val, high_val)
print("Partitioned array:", partitioned_arr)
