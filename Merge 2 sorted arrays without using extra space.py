def next_gap(gap):
    if gap <= 1:
        return 0
    return (gap // 2) + (gap % 2)

def merge(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    gap = next_gap(n + m)
    
    while gap > 0:
        # Compare elements in the first array
        i = 0
        while i + gap < n:
            if arr1[i] > arr1[i + gap]:
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
            i += 1

        # Compare elements between the two arrays
        j = gap - n if gap > n else 0
        while i < n and j < m:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1

        # Compare elements in the second array
        if j < m:
            j = 0
            while j + gap < m:
                if arr2[j] > arr2[j + gap]:
                    arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]
                j += 1

        gap = next_gap(gap)

# Example usage
arr1 = [1, 4, 7, 8, 10]
arr2 = [2, 3, 9]

merge(arr1, arr2)

print("First array after merging:", arr1)
print("Second array after merging:", arr2)
