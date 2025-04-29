import tkinter as tk
from tkinter import ttk


def FrameRoomLeft(parent, saved_data, controller):
    """ Фрейм с элементами управления для редактирования помещения. """   
    # Создание фрейма    
    control_frame = ttk.Frame(parent)

    # Верхний фрейм управления
    frame = ttk.LabelFrame(control_frame, text="Редактирование помещения", padding="3") 
    frame.grid(row=0, column=0, sticky='nsew')
    # Поля выбора типа добавляемого элемента
    #dor_win_var = tk.IntVar(1)  # 1 - Окно (по умолчанию), 0 - Дверь
    door = ttk.Radiobutton(frame, text="Дверь", value=0)
    door.grid(sticky="w", row=0, column=0, padx=5, pady=5)
    window = ttk.Radiobutton(frame, text="Окно", value=1)
    window.grid(sticky="w", row=1, column=0, padx=5, pady=5)

    # Размеры
    ttk.Label(frame, text="Ширина двери:").grid(sticky="e", row=0, column=1)
    ttk.Spinbox(frame, from_=30, to=300, increment=5, state="readonly", width=3).grid(sticky="e",row=0, column=2)
    ttk.Label(frame, text="Ширина окна:").grid(sticky="e",row=1, column=1)
    ttk.Spinbox(frame, from_=30, to=600, increment=5, state="readonly", width=3).grid(sticky="e",row=1, column=2)
    
    # Кнопки управления
    btn_add = ttk.Button(control_frame, text="Добавить элемент", command=add_element)
    btn_add.grid(row=1, column=0, sticky='w', padx=10, pady=5) #pack(anchor='w', padx=10, pady=5)
    btn_del = ttk.Button(control_frame, text="Удалить выбранный элемент", command=del_element)
    btn_del.grid(row=2, column=0, sticky='w', padx=10, pady=5) #pack(anchor='w', padx=10, pady=5)
    btn_rotate_all = ttk.Button(control_frame, text="Повернуть проект", command=rotate_element)
    btn_rotate_all.grid(row=3, column=0, sticky='w', padx=10, pady=5) #pack(anchor='w', padx=10, pady=5)
    btn_rotate = ttk.Button(control_frame, text="Повернуть выбранный элемент", command=rotate_element)
    btn_rotate.grid(row=4, column=0, sticky='w', padx=10, pady=5) #pack(anchor='w', padx=10, pady=5)
 

    return control_frame
    
def add_element():
    print("Добавить")

def del_element():
    print("Удалить")

def rotate_element():
    print("Повернуть")
