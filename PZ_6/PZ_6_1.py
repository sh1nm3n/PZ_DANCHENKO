'''
Вариант 9.
Дан целочисленный список размера 10. Вывести вначале все содержащиеся в данном
списке четные числа в порядке возрастания их индексов, а затем — все нечетные
числа в порядке убывания их индексов.
'''
import random

random_numbers = [random.randint(1, 10) for _ in range(10)]
print("Сгенерированный список:", random_numbers)


chetnie_num = [num for num in random_numbers if num % 2 == 0]
nechetnie_num = [num for num in random_numbers if num % 2 != 0]


print("Четные числа в порядке возрастания индексов:", chetnie_num)
print("Нечетные числа в порядке убывания индексов:", nechetnie_num[::-1])