'''
Вариант 9.
Дано число N (>0) и символы C1 и C2. Вывести строку длины N, которая
состоит из чередующихся символов C1 и C2, начиная с C1.
'''
def N_string(N, C1, C2):
    if N <= 0 or N % 2 != 0:
        return "N должно быть четным и больше 0."
    result = (C1 + C2) * (N // 2)
    return result


def is_int(x):    #Проверка числа
    while type(x) != int:
        try:
            x = int(x)
            return x
        except ValueError:
            print('Вы ввели число не правильно')
            x = input('Повторите попытку: ')

N = input("Введите четное число N (>0): ")
N = is_int(N)
C1 = input("Введите первый символ: ")
C2 = input("Введите второй символ: ")

alt_string = N_string(N, C1, C2)
print(alt_string)
