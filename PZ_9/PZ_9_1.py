'''
Вариант 9
Дана строка '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15', отражающая
средние температуры по месяцам в году. Преобразовать информацию из строки в
словарь, с использованием функции найти среднюю и минимальные температуры,
результаты вывести на экран.
'''
data = '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15'

parts = data.split()

year = parts[0]

months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
          'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

temperatures = {months[i]: int(parts[i+1]) for i in range(12)}

def average_temp(x):
    return sum(x.values()) / len(x)

def min_temp(x):
    return min(x.values())

avg_temp = average_temp(temperatures)
minimum_temp = min_temp(temperatures)

print(f"Средняя температура за {year}: {avg_temp:.1f}°C")
print(f"Минимальная температура за {year}: {minimum_temp}°C")