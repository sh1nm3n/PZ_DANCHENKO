#Вариант 9

class Calculator:

    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b


if __name__ == "__main__":
    calc = Calculator()

    print("Сложение:", calc.addition(5, 3))  # 8
    print("Вычитание:", calc.subtraction(10, 4))  # 6
    print("Умножение:", calc.multiplication(7, 2))  # 14

    try:
        print("Деление:", calc.division(15, 3))  # 5.0
        print("Деление:", calc.division(5, 0))  # Вызовет исключение
    except ValueError as e:
        print("Ошибка:", e)