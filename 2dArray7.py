def generate_spiral_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    start_row, end_row = 0, n - 1
    start_col, end_col = 0, n - 1
    num = 1

    while num <= n * n:

        for j in range(start_col, end_col + 1):
            matrix[start_row][j] = num
            num += 1
        start_row += 1


        for i in range(start_row, end_row + 1):
            matrix[i][end_col] = num
            num += 1
        end_col -= 1


        for j in range(end_col, start_col - 1, -1):
            matrix[end_row][j] = num
            num += 1
        end_row -= 1


        for i in range(end_row, start_row - 1, -1):
            matrix[i][start_col] = num
            num += 1
        start_col += 1

    return matrix
n = 3
result = generate_spiral_matrix(n)
for row in result:
    print(row)
