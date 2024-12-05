'''
Вариант 9.
Описать функцию Swap(X, Y), меняющую содержимое переменных X и Y (X и Y —
вещественные параметры, являющиеся одновременно входными и выходными). С
ее помощью для данных переменных A, B, C, D последовательно поменять
содержимое следующих пар: A и B, C и D, B и C и вывести новые значения A, B, C,
D.
'''
def swap(x, y):
    return y, x

def is_int(x):    #Проверка числа
    while type(x) != int:
        try:
            x = int(x)
            return x
        except ValueError:
            print('Вы ввели число не правильно')
            x = input('Повторите попытку: ')


A = input("Введите число A: ")
A = is_int(A)

B = input("Введите число B: ")
B = is_int(B)

C = input("Введите число C: ")
C = is_int(C)

D = input("Введите число D: ")
D = is_int(D)

A, B = swap(A, B)
C, D = swap(C, D)
B, C = swap(B, C)

print(f"Новые значения: A = {A}, B = {B}, C = {C}, D = {D}")