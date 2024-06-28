def find_common_elements(arr1, arr2, arr3):
    i, j, k = 0, 0, 0
    common_elements = []

    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        # If the elements at current indices are equal, add to the result
        if arr1[i] == arr2[j] == arr3[k]:
            common_elements.append(arr1[i])
            i += 1
            j += 1
            k += 1
        # Move the pointer which is pointing to the smallest element
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1
arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

common = find_common_elements(arr1, arr2, arr3)
print(common)
