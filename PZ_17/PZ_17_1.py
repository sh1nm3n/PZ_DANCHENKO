#Вариант 20 (9й вариант не открывается)
import tkinter as tk
from tkinter import ttk


def create_login_form():
    root = tk.Tk()
    root.title("Форма регистрации")
    root.geometry("400x500")

    style = ttk.Style()
    style.configure("Header.TLabel", font=("Arial", 10, "bold"))

    login_frame = ttk.LabelFrame(root, text="User login info", padding=10)
    login_frame.pack(pady=10, padx=10, fill="x")

    ttk.Label(login_frame, text="Username:", style="Header.TLabel").grid(row=0, column=0, sticky="w")
    username_entry = ttk.Entry(login_frame)
    username_entry.grid(row=0, column=1, sticky="ew", pady=5)

    ttk.Label(login_frame, text="Email:", style="Header.TLabel").grid(row=1, column=0, sticky="w")
    email_entry = ttk.Entry(login_frame)
    email_entry.grid(row=1, column=1, sticky="ew", pady=5)

    ttk.Label(login_frame, text="Password:", style="Header.TLabel").grid(row=2, column=0, sticky="w")
    password_entry = ttk.Entry(login_frame, show="*")
    password_entry.grid(row=2, column=1, sticky="ew", pady=5)

    ttk.Separator(root, orient="horizontal").pack(fill="x", pady=10)

    personal_frame = ttk.LabelFrame(root, text="Data diri", padding=10)
    personal_frame.pack(pady=10, padx=10, fill="x")

    ttk.Label(personal_frame, text="Alamat:", style="Header.TLabel").grid(row=0, column=0, sticky="w")
    address_entry = ttk.Entry(personal_frame)
    address_entry.grid(row=0, column=1, sticky="ew", pady=5)

    ttk.Label(personal_frame, text="Tanggal lahir:", style="Header.TLabel").grid(row=1, column=0, sticky="w")
    birth_entry = ttk.Entry(personal_frame)
    birth_entry.grid(row=1, column=1, sticky="ew", pady=5)

    ttk.Label(personal_frame, text="Usia:", style="Header.TLabel").grid(row=2, column=0, sticky="w")
    age_entry = ttk.Entry(personal_frame)
    age_entry.grid(row=2, column=1, sticky="ew", pady=5)

    gender_var = tk.StringVar()
    ttk.Label(personal_frame, text="Jenis kelamin:", style="Header.TLabel").grid(row=3, column=0, sticky="w")
    ttk.Radiobutton(personal_frame, text="Pria", variable=gender_var, value="Pria").grid(row=3, column=1, sticky="w")
    ttk.Radiobutton(personal_frame, text="Wanita", variable=gender_var, value="Wanita").grid(row=4, column=1,
                                                                                             sticky="w")

    agree_var = tk.IntVar()
    ttk.Checkbutton(root, text="Saya bersedia mengikuti aturan forum", variable=agree_var).pack(pady=10)

    button_frame = ttk.Frame(root)
    button_frame.pack(pady=10)

    ttk.Button(button_frame, text="Reset", command=lambda: reset_form(
        username_entry, email_entry, password_entry,
        address_entry, birth_entry, age_entry, gender_var, agree_var
    )).grid(row=0, column=0, padx=5)

    ttk.Button(button_frame, text="Submit", command=submit_form).grid(row=0, column=1, padx=5)

    root.mainloop()


def reset_form(*entries):
    for entry in entries[:-2]:
        entry.delete(0, tk.END)
    entries[-2].set("")
    entries[-1].set(0)

def submit_form():
    print("Форма отправлена!")


if __name__ == "__main__":
    create_login_form()