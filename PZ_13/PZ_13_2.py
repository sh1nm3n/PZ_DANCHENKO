# Вариант 9

matrix = [
    [1, -3, 6],
    [9, 4, 12],
    [0, 15, -6]
]

numbers = []
for row in matrix:
    for x in row:
        if x > 0 and x % 3 == 0:
            numbers.append(x)

if numbers:
    avg = sum(numbers) / len(numbers)
    print(f"Среднее: {avg:.1f}")
else:
    print("Нет подходящих чисел")