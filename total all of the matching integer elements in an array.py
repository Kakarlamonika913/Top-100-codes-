def sum_of_matching_elements(arr):
    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    return sum(duplicates) 
arr = [1, 2, 3, 2, 4, 3, 5, 6, 5]
print(sum_of_matching_elements(arr))
