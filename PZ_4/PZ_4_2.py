'''
Дано число A (> 1). Вывести наименьшее из целых чисел K,
для которых сумма 1+1/2 + ... + 1/K будет больше A, и саму эту сумму.
'''

def find_k_greater_than_a(A):
    if A <= 1:
        return "A должно быть больше 1"

    total_sum = 0
    K = 0
    while total_sum <= A:
        K += 1
        total_sum += 1 / K
    return K, total_sum


def is_int(x):    #Проверка числа
    while type(x) != int:
        try:
            x = int(x)
            return x
        except ValueError:
            print('Вы ввели число не правильно')
            x = input('Повторите попытку: ')


A = input("Введите число A (> 1): ")
A = is_int(A)
K, total_sum = find_k_greater_than_a(A)
print(f"Наименьшее целое число K: {K}")
print(f"Сумма 1 + 1/2 + ... + 1/K: {total_sum}")
