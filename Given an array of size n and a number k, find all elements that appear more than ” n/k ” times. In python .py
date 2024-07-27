def find_elements(arr, k):
    n = len(arr)
    if k == 0:
        return []

    # Step 1: Count frequencies of elements
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Step 2: Filter elements based on the condition
    result = []
    for num, count in frequency.items():
        if count > n // k:
            result.append(num)

    return result

# Example usage
arr = [1, 2, 3, 1, 2, 1, 1, 3, 3, 3, 3]
k = 4
print(find_elements(arr, k))  # Output: [1, 3]
