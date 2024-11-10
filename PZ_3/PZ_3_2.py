'''
Вар. 9
Арифметические действия над числами пронумерованы следующим образом: 1 —
сложение, 2 — вычитание, 3 — умножение, 4 — деление. Дан номер действия N
(целое число в диапазоне 1-4) и вещественные числа A и B (В не равно 0). Выполнить
над числами указанное действие и вывести результат.
'''

def sum(A, B):
    return A + B

def sub(A, B):
    return A - B

def mltp(A, B):
    return A * B

def div(A, B):
    return A / B

while True: #Проверка действия на целое число от 1 до 4
    N = input("Введите число от 1 до 4 (1 = сложение, 2 = вычитание, 3 = умножение, 4 = деление): ")
    try:
        operation = int(N)
        if operation < 1 or operation > 4:
            print("Число должно быть от 1 до 4.")
            continue
        break
    except ValueError:
        print("Ошибка! Повторите попытку.")


A = float(input("Введите первое вещественное число A: "))
B = float(input("Введите второе вещественное число B: "))

if operation == 1:
    result = sum(A,B)
    print("Результат сложения: ", result)
elif operation == 2:
    result = sub(A,B)
    print("Результат вычитания: ", result)
elif operation == 3:
    result = mltp(A,B)
    print("Результат умножения: ", result)
elif operation == 4:
    result = div(A,B)
    print("Результат деления: ", result)


