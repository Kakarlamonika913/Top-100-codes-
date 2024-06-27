def sort_array(arr):
    count0 = arr.count(0)
    count1 = arr.count(1)
    count2 = arr.count(2)
    
    return [0] * count0 + [1] * count1 + [2] *
arr = [2, 0, 2, 1, 1, 0]
sorted_arr = sort_array(arr)
print(sorted_arr)
