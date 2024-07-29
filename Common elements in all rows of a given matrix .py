def find_common_elements(matrix):
    if not matrix:
        return []

    # Initialize the set with the first row
    common_elements = set(matrix[0])

    # Iterate over the remaining rows and update the set
    for row in matrix[1:]:
        common_elements &= set(row)

    # Convert the set to a list to return
    return list(common_elements)

# Example usage
matrix = [
    [1, 2, 3, 4],
    [2, 4, 6, 8],
    [2, 4, 8, 10]
]

print(find_common_elements(matrix))  # Output: [2, 4]
