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
    num_str = str(number)
    for i in range(len(num_str)):  #проходим по каждой цифре
        for j in range(i + 1, len(num_str)):  #сравниваем с остальными цифрами
            if num_str[i] == num_str[j]: #если нашли одинаковые цифры
                return True
    return False


gen_num = gen_rand_num()
print(f"Сгенерированное четырехзначное число: {gen_num}")


if has_duplicate_digits(gen_num):
    print("В числе есть одинаковые цифры.")
else:
    print("В числе нет одинаковых цифр.")





