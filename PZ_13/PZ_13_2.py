# Вариант 9
def avg_positive_multiples_of_three(matrix):
    filtered = [num for row in matrix
                for num in row
                if num > 0 and num % 3 == 0]

    return sum(filtered) / len(filtered) if filtered else 0

matrix = [
    [1, -3, 6],
    [9, 4, 12],
    [0, 15, -6]
]

result = avg_positive_multiples_of_three(matrix)
print(result)