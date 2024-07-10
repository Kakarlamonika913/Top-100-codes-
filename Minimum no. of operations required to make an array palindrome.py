def min_operations_to_make_palindrome(arr):
    # Initialize pointers for the start and end of the array
    left = 0
    right = len(arr) - 1
    operations = 0
    
    while left < right:
        if arr[left] == arr[right]:
            # If the elements are the same, move both pointers towards the center
            left += 1
            right -= 1
        elif arr[left] < arr[right]:
            # If the left element is smaller, merge it with the next one on the left
            arr[left + 1] += arr[left]
            left += 1
            operations += 1
        else:
            # If the right element is smaller, merge it with the previous one on the right
            arr[right - 1] += arr[right]
            right -= 1
            operations += 1
            
    return operations

# Example usage
arr = [1, 4, 5, 1]
print("Minimum operations to make palindrome:", min_operations_to_make_palindrome(arr))
