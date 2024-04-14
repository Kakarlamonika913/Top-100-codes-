def is_subset(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    return set1.issubset(set2)

arr1 = [1, 2, 3]
arr2 = [1, 2, 3, 4, 5]

if is_subset(arr1, arr2):
    print("arr1 is a subset of arr2")
else:
    print("arr1 is not a subset of arr2")
