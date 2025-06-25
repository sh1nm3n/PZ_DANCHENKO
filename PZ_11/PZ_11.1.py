#Вариант 9.

with open('numbers.txt', 'w', encoding='utf-8') as f:
    f.write("10 -5 3 8 -2 15 7 -8 12 6 -10 4")

with open('numbers.txt', 'r', encoding='utf-8') as f:
    numbers = list(map(int, f.read().split()))

count = len(numbers)
max_val = max(numbers)
max_index = len(numbers) - 1 - numbers[::-1].index(max_val)

third = len(numbers) // 3
new_numbers = numbers[-third:] + numbers[third:-third] + numbers[:third]

with open('result_numbers.txt', 'w', encoding='utf-8') as f:
    f.write("Исходные данные: " + ' '.join(map(str, numbers)) + "\n")
    f.write(f"Количество элементов: {count}\n")
    f.write(f"Индекс последнего максимального элемента: {max_index}\n")
    f.write("Меняем местами первую и последнюю трети: " + ' '.join(map(str, new_numbers)))