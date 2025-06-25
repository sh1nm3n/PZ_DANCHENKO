# Вариант 9

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_col = [10, 11, 12]

for i in range(3):
    matrix[i][1] = new_col[i]

for row in matrix:
    print(row)