def smallest_subarray(arr, target):
    n = len(arr)
    min_length = n + 1
    current_sum = 0
    start = 0
    
    for end in range(n):
        current_sum += arr[end]
        
        while current_sum > target:
            min_length = min(min_length, end - start + 1)
            current_sum -= arr[start]
            start += 1
            
    return min_length if min_length <= n else 0
arr = [1, 4, 45, 6, 0, 19]
target = 51
print(f"The smallest subarray length is: {smallest_subarray(arr, target)}")
