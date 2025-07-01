'''Практическая работа 2(вариант 9). Даны целые положительные числа A и B (A > B). На отрезке длины A
размещено максимально возможное количество отрезков длины B (без наложений).
Используя операцию деления нацело, найти количество отрезков B, размещенных на
отрезке A.'''
import tkinter as tk
from tkinter import messagebox


def calculate_segments():
    try:
        A = int(entry_A.get())
        B = int(entry_B.get())

        if A <= 0 or B <= 0:
            messagebox.showerror("Ошибка", "Числа должны быть положительными!")
            return

        if A <= B:
            messagebox.showerror("Ошибка", "A должно быть больше B!")
            return

        result = A // B
        label_result.config(text=f"Количество отрезков B на отрезке A: {result}")

    except ValueError:
        messagebox.showerror("Ошибка", "Введите целые числа!")


root = tk.Tk()
root.title("Расчет отрезков")
root.geometry("400x200")

label_A = tk.Label(root, text="Введите длину отрезка A (целое число > 0):")
label_A.pack(pady=5)

entry_A = tk.Entry(root)
entry_A.pack(pady=5)

label_B = tk.Label(root, text="Введите длину отрезка B (целое число > 0, меньше A):")
label_B.pack(pady=5)

entry_B = tk.Entry(root)
entry_B.pack(pady=5)

btn_calculate = tk.Button(root, text="Рассчитать", command=calculate_segments)
btn_calculate.pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 10, "bold"))
label_result.pack(pady=10)

root.mainloop()