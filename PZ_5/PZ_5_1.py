'''
Вариант 9.
Составить программу, в которой функция генерирует четырехзначное число и
определяет, есть ли в числе одинаковые цифры
'''
import random


def gen_rand_num():
    number = random.randint(1000, 9999)
    return number

def has_duplicate_digits(number):
    a = number // 1000 #первая цифра числа
    b = (number // 100) % 10 #вторая цифра числа
    c = (number // 10) % 10 #третья цифра числа
    d = number % 10 #четвертая цифра числа
    if a == b or a == c or a == d or b == c or b == d or c == d:
        return True
    else:
        return False

gen_num = gen_rand_num()
print(f"Сгенерированное четырехзначное число: {gen_num}")


if has_duplicate_digits(gen_num):
    print("В числе есть одинаковые цифры.")
else:
    print("В числе нет одинаковых цифр.")





