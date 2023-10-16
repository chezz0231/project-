import tkinter as tk
from tkinter import ttk
import sqlite3


def add_employee():
    fio = fio_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    salary = salary_entry.get()
    conn.execute("INSERT INTO employees (fio, phone, email, salary) VALUES (?, ?, ?, ?)", (fio, phone, email, salary))
    conn.commit()

def update_employee():
    fio = fio_combobox.get()
    phone = phone_entry.get()
    email = email_entry.get()
    salary = salary_entry.get()
    conn.execute("UPDATE employees SET phone = ?, email = ?, salary = ? WHERE fio = ?", (phone, email, salary, fio))
    conn.commit()

def delete_employee():
    fio = fio_combobox.get()
    conn.execute("DELETE FROM employees WHERE fio = ?", (fio,))
    conn.commit()

def search_employee():
    fio = search_entry.get()
    cursor = conn.execute("SELECT * FROM employees WHERE fio LIKE ?", ('%' + fio + '%',))
    for row in cursor:
        print(row)

conn = sqlite3.connect('company.db')
conn.execute("CREATE TABLE IF NOT EXISTS employees (fio TEXT, phone TEXT, email TEXT, salary REAL)")
root = tk.Tk()
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)
ttk.Label(frame, text="ФИО:").grid(row=0, column=0, sticky=tk.W)
fio_entry = ttk.Entry(frame)
fio_entry.grid(row=0, column=1)

ttk.Label(frame, text="Телефон:").grid(row=1, column=0, sticky=tk.W)
phone_entry = ttk.Entry(frame)
phone_entry.grid(row=1, column=1)

ttk.Label(frame, text="Email:").grid(row=2, column=0, sticky=tk.W)
email_entry = ttk.Entry(frame)
email_entry.grid(row=2, column=1)

ttk.Label(frame, text="Заработная плата:").grid(row=3, column=0, sticky=tk.W)
salary_entry = ttk.Entry(frame)
salary_entry.grid(row=3, column=1)

add_button = ttk.Button(frame, text="Добавить", command=add_employee)
add_button.grid(row=4, column=0, columnspan=2, pady=10)

ttk.Label(frame, text="Выберите сотрудника:").grid(row=5, column=0, sticky=tk.W)
fio_combobox = ttk.Combobox(frame)
fio_combobox.grid(row=5, column=1)

ttk.Label(frame, text="Телефон:").grid(row=6, column=0, sticky=tk.W)
phone_entry = ttk.Entry(frame)
phone_entry.grid(row=6, column=1)

ttk.Label(frame, text="Email:").grid(row=7, column=0, sticky=tk.W)
email_entry = ttk.Entry(frame)
email_entry.grid(row=7, column=1)

ttk.Label(frame, text="Заработная плата:").grid(row=8, column=0, sticky=tk.W)
salary_entry = ttk.Entry(frame)
salary_entry.grid(row=8, column=1)

update_button = ttk.Button(frame, text="Изменить", command=update_employee)
update_button.grid(row=9, column=0, columnspan=2, pady=10)

ttk.Label(frame, text="Выберите сотрудника:").grid(row=10, column=0, sticky=tk.W)
fio_combobox = ttk.Combobox(frame)
fio_combobox.grid(row=10, column=1)

delete_button = ttk.Button(frame, text="Удалить", command=delete_employee)
delete_button.grid(row=11, column=0, columnspan=2, pady=10)

ttk.Label(frame, text="Введите ФИО:").grid(row=12, column=0, sticky=tk.W)
search_entry = ttk.Entry(frame)
search_entry.grid(row=12, column=1)

search_button = ttk.Button(frame, text="Найти", command=search_employee)
search_button.grid(row=13, column=0, columnspan=2, pady=10)

root.mainloop()

conn.close()