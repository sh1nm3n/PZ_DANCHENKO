'''
Вариант 9.
Составить программу, в которой функция генерирует четырехзначное число и
определяет, есть ли в числе одинаковые цифры
'''
import random

def gen_rand_num():
    return random.randint(1000, 9999)


def same_digits(number):
    digits = str(number)
    return len(set(digits)) < len(digits) #Сравниваем длину множества уникальных цифр с длиной строки


number = gen_rand_num()
print(f"Сгенерированное четырехзначное число: {number}")

if same_digits(number):
    print("В числе есть одинаковые цифры.")
else:
    print("В числе нет одинаковых цифр.")




