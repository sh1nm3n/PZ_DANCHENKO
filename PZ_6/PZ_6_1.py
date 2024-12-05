'''
Вариант 9.
Дан целочисленный список размера 10. Вывести вначале все содержащиеся в данном
списке четные числа в порядке возрастания их индексов, а затем — все нечетные
числа в порядке убывания их индексов.
'''
numbers = [10, 17, 20, 25, 30, 33, 40, 45, 50, 55]

chetnie_numbers = []
nechetnie_numbers = []

#разделение чисел на четные и нечетные
for number in numbers:
    if number % 2 == 0:
        chetnie_numbers.append(number)
    else:
        nechetnie_numbers.append(number)

print("Четные числа: ", chetnie_numbers)

print("Нечетные числа: ", nechetnie_numbers[::-1])