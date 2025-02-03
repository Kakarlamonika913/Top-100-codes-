def find_max(arr):
    if not arr:
        return None  # Handle empty array case
    return max(arr)
arr = [10, 25, 37, 49, 5]
print("Maximum element:", find_max(arr))
