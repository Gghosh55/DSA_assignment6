def search_matrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])

    left = 0
    right = rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        row = mid // cols
        col = mid % cols

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            right = mid - 1
        else:
            left = mid + 1

    return False
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 3

print(search_matrix(matrix, target))
