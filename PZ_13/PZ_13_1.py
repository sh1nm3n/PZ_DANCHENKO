# Вариант 9

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Новый столбец
new_col = [10, 11, 12]

# Замена второго столбца
for i in range(3):
    matrix[i][1] = new_col[i]

# Вывод результата
for row in matrix:
    print(row)