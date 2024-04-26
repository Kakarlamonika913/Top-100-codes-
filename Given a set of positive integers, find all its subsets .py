from itertools import chain, combinations

def all_subsets(nums):
    return chain(*[combinations(nums, i) for i in range(len(nums) + 1)])
nums = {1, 2, 3}
subsets = list(all_subsets(nums))
print(subsets)f
