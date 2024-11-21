'''
Вариант 9.
Дано целое число N (>0). Найти сумму 1 + 1/2 + 1/3 + ... + 1/N
'''

def sum(a):
    while a <= 0:
        return "N должно быть больше 0"

    total_sum = 0
    for i in range(1, N + 1 ):
        total_sum += 1 / i
    return total_sum

def is_int(x):    #Проверка числа
    while type(x) != int:
        try:
            x = int(x)
            return x
        except ValueError:
            print('Вы ввели число не правильно')
            x = input('Повторите попытку: ')


N = input("Введите целое число: ")
N = is_int(N)
sum1 = sum(N)
print(f"Сумма = {sum1}")
