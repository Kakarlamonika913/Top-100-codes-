def unique_elements(arr):
    unique_list = []
    for num in arr:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list

arr = [1, 2, 3, 2, 4, 3, 5, 6, 5]
print(unique_elements(arr))
