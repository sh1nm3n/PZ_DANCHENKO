'''
Вар. 9
Даны два целых числа: A, B.
Проверить истинность высказывания: «Хотя бы одно из чисел A и B нечетное».
'''

A = input("Введите первое целое число: ")
while type(A) != int:  #проверка на целое число
      try:
            A = int(A)
      except:
            print("Ошибка!")
            A = input ("Повторите попытку. ")

B = input("Введите второе целое число: ")
while type(B) != int:
    try:
        B = int(B)
    except:
        print("Ошибка!")
        B = input("Повторите попытку. ")

if A % 2 != 0 or B % 2 != 0:
    print("True")
else:
    print("False")
