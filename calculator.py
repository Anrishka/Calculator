# Калькулятор

import tkinter as tk
from asteval import Interpreter
from tkinter import messagebox
import ctypes

try:
	ctypes.windll.shcore.SetProcessDpiAwareness(True)
except Exception:
	pass

# Создаем главное окно приложения
root = tk.Tk()

# Настраиваем размер, фон, возможность изменения размера и заголовок окна
root.geometry('260x300')
root.config(bg='black')
root.resizable(False, False)
root.title('+-*/')

# Установка иконки окна
root.iconbitmap(r'C:\Users\user\Desktop\курс питон записи\GPT_tasks\graphic_calculator\icon.ico')

# Поместим интерпретатор для вычислений в переменную
interpreter = Interpreter()

# Функция для очистки поля ввода
def clear_input(event=None):
	entry_text.set('')

# Функция для добавления символов в поле ввода
def update_entry(text):
    current = entry_text.get()
    entry_text.set(current + text)

# Отдельно создадим функцию для биндов, чтобы указать тут аргумент event, так как оригинальная функция уже принимает один аргумент
def update_entry_bind(event):
    current = entry_text.get()
    entry_text.set(current + event.char)

# Функция для вычисления введенного выражения
def calculate_expression(event=None):
    expression = entry_text.get()
    result = interpreter(expression)  
    if interpreter.error: 
        messagebox.showerror("Ошибка", "\nВведите выражение корректно!")
        interpreter.error = []  
        entry_text.set("")  
    else:
        entry_text.set(result)


# Функция для вычисления квадратного корня из числа
def calculate_square(event=None):
	expression = entry_text.get()
	try:
		result = interpreter.eval(f'sqrt({expression})')
		if result == int(result):
			result = int(result)
		entry_text.set(result)
	except Exception as e: 
		messagebox.showerror(f"Ошибка", "\nВведите выражение корректно!")
		interpreter.error = []  
		entry_text.set("")


# Функция для удаления последнего символа в поле ввода
def delete_last_charecter(event):
	current_text = entry_text.get()
	updated_text = current_text[:-1]
	entry_text.set(updated_text)


# Создаем и настраиваем поле ввода
entry_text = tk.StringVar()
f_entry = tk.Entry(root, textvariable=entry_text, state='readonly', font=('Arial', 12), justify=tk.CENTER)
f_entry.pack()

# Привяжем наши функции к клавишам для удобства
root.bind('<Key>', update_entry_bind)
root.bind('<Return>', calculate_expression)
root.bind('<BackSpace>', delete_last_charecter)
root.bind('<Control-Return>', calculate_square)
root.bind('<Control-BackSpace>', clear_input)

# Создаем фрейм для кнопок
f_buttons = tk.Frame(root)
f_buttons.pack()

# Список цифр для кнопок калькулятора
digit_buttons_list = [
	'1', '2', '3',
	'4', '5', '6',
	'7', '8', '9',
	'0'
]

# Переменные для управления расположением кнопок цифр
column_for_digits = 0
row_for_digits = 0

# Создание кнопок цифр в цикле
for i in digit_buttons_list: 
	digit_button = tk.Button(f_buttons, text=i, font=('Arial', 8), padx=12, pady=4, bg='black', fg='white', command=lambda i=i: update_entry(i))
	digit_button.grid(column=column_for_digits, row=row_for_digits, sticky='nsew')
	column_for_digits += 1
	if column_for_digits == 3:  # Переход на новую строку после каждых трех кнопок
		column_for_digits = 0
		row_for_digits += 1

# Список симполов для кнопок калькулятора
symbols_list = ['(', ')', '+', '-', '*', '/', '.']

# Переменные для управления расположением кнопок символов
column_for_symbols = 1
row_for_symbols = 3

# Создание кнопок символов в цикле
for i in symbols_list: 
	symbol_button = tk.Button(f_buttons, text=i, font=('Arial', 8), padx=12, pady=4, bg='black', fg='white', command=lambda i=i: update_entry(i)).grid(column=column_for_symbols, row=row_for_symbols, sticky='nsew')
	column_for_symbols += 1
	if column_for_symbols == 3: # Переход на новую строку после каждых трех кнопок
		column_for_symbols = 0
		row_for_symbols += 1

# Создание кнопок действий с отдельными функциями
result = tk.Button(f_buttons, text='=', font=('Arial', 8), padx=12, pady=4, bg='black', fg='white', command=calculate_expression)
result.grid(column=2, row=5, sticky='nsew')

square_root = tk.Button(f_buttons, text='√', font=('Arial', 8), padx=12, pady=4, bg='black', fg='white', command=calculate_square)
square_root.grid(column=0, row=6, sticky='nsew')

clear = tk.Button(f_buttons, text="C", font=('Arial', 8), padx=12, pady=4, bg='black', fg='white', command=clear_input)
clear.grid(column=1, row=6, sticky='nsew')

backspace = tk.Button(f_buttons, text="←", font=('Arial', 8), padx=12, pady=4, bg='black', fg='white', command=delete_last_charecter)
backspace.grid(column=2, row=6, sticky='nsew')

# Запускаем цикл приложения
root.mainloop()



















































