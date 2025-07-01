# Вариант 9
def replace_second_column(matrix, new_column):
    return [row[:1] + [new_val] + row[2:]
            for row, new_val in zip(matrix, new_column)]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
new_column = [10, 11, 12]

result = replace_second_column(matrix, new_column)
print(result)