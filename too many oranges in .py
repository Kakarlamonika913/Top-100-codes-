def can_achieve_exact_slices(num_oranges, target_slices):
    min_possible_slices = num_oranges * 10
    max_possible_slices = num_oranges * 12
    return min_possible_slices <= target_slices <= max_possible_slices

test_cases = int(input())
results = []
for _ in range(test_cases):
    num_oranges, target_slices = map(int, input().split())
    if can_achieve_exact_slices(num_oranges, target_slices):
        results.append("YES")
    else:
        results.append("NO")

print("\n".join(results))
