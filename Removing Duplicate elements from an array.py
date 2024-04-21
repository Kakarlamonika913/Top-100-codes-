def remove_duplicates(arr):
    unique_list = []
    for item in arr:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
my_array = [1, 2, 3, 3, 4, 5, 5, 6]
result = remove_duplicates(my_array)
print(result)
