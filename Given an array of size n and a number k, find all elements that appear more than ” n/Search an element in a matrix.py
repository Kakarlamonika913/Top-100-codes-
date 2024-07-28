def search_sorted_matrix(matrix, target):
    if not matrix:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    # Start from the top-right corner
    r, c = 0, cols - 1

    while r < rows and c >= 0:
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] > target:
            c -= 1
        else:
            r += 1

    return False

# Example usage
matrix = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9
