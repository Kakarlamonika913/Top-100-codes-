def are_disjoint(arr1, arr2):
    for element in arr1:
        if element in arr2:
            return False
    return True

arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 7, 8, 9, 10]
print(are_disjoint(arr1, arr2))

arr3 = [1, 2, 3]
arr4 = [3, 4, 5]
print(are_disjoint(arr3, arr4))
