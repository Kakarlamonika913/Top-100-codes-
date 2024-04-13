arr1 = [3, 5, 2, 8, 1]
arr2 = [1, 5, 2, 3, 8]

sorted_arr = sorted(arr1, key=lambda x: arr2.index(x))
print(sorted_arr)
