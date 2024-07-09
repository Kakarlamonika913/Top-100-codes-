def find_median_sorted_arrays(arr1, arr2):
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1  # Ensure arr1 is the smaller array

    x, y = len(arr1), len(arr2)
    low, high = 0, x

    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (x + y + 1) // 2 - partitionX

        maxX = float('-inf') if partitionX == 0 else arr1[partitionX - 1]
        minX = float('inf') if partitionX == x else arr1[partitionX]

        maxY = float('-inf') if partitionY == 0 else arr2[partitionY - 1]
        minY = float('inf') if partitionY == y else arr2[partitionY]

        if maxX <= minY and maxY <= minX:
            if (x + y) % 2 == 0:
                return (max(maxX, maxY) + min(minX, minY)) / 2
            else:
                return max(maxX, maxY)
        elif maxX > minY:
            high = partitionX - 1
        else:
            low = partitionX + 1

    raise ValueError("Input arrays are not sorted")

# Example usage
arr1 = [1, 3, 8]
arr2 = [7, 9, 10]
median = find_median_sorted_arrays(arr1, arr2)
print(median)
