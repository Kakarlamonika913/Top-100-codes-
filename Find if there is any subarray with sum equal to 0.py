def hasZeroSumSubarray(arr):
    sums_map = {}
    sum_so_far = 0

    for i in range(len(arr)):
        sum_so_far += arr[i]

        if sum_so_far == 0 or arr[i] == 0 or sum_so_far in sums_map:
            return True

        sums_map[sum_so_far] = i

    return False


arr1 = [1, 2, -2, 4, -4, -1, 1, -3, 3]
arr2 = [1, 2, 3, 4, 5] 

print(f"Output for arr1: {hasZeroSumSubarray(arr1)}")
print(f"Output for arr2: {hasZeroSumSubarray(arr2)}")
