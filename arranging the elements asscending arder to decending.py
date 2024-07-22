def arrange_ascending_descending(arr):
    arr.sort()
    mid = len(arr) // 2
    first_half = arr[:mid]
    second_half = arr[mid:]
    second_half.reverse()
    arranged_arr = first_half + second_half

    return arranged_arr

# Example usage:
arr = [3, 1, 2, 4, 6, 5]
arranged_arr = arrange_ascending_descending(arr)
print(arranged_arr)
