'''
Вар. 9
Даны два целых числа: A, B.
Проверить истинность высказывания: «Хотя бы одно из чисел A и B нечетное».
'''

# Функция для проверки, является ли число нечетным
def is_odd(n):
    return n % 2 != 0

# Ввод чисел A и B с обработкой исключений
while True:
    A = input("Введите число A: ")
    try:
        num1 = int(A)
        if num1 == 0:
            print("ne")
            continue
        break
    except ValueError:
        print("Ошибка: Пожалуйста, введите целое число.")

while True:
    B = input("Введите число B: ")
    try:
        num2 = int(B)
        if num1 == 0:
            print("ne")
            continue
        break
    except ValueError:
        print("Ошибка: Пожалуйста, введите целое числа.")

if is_odd(num1) or is_odd(num2):
    print("Истинно: хотя бы одно из чисел A и B нечетное.")
else:
    print("Ложно: оба числа четные.")
