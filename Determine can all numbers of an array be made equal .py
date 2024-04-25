def can_be_made_equal(arr):
    max_num = max(arr)
    min_num = min(arr)
    if max_num == min_num:
        return True
    diff = max_num - min_num
    return diff == 0 or all(num % diff == 0 for num in arr)
arr = [4, 4, 6, 4, 10]
print(can_be_made_equal(arr)) 
