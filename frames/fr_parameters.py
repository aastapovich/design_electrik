# fr_parameters.py
import tkinter as tk
from tkinter import ttk
from logic.logic_table import TableManager



def FrameParameters(parent, saved_data, controller):
    """ Фрейм с параметрами. """

    frame_parameters = ttk.Frame(parent)


    lbl_title = ttk.Label(frame_parameters, text="Параметры", font=("Arial", 14, "bold"))
    lbl_title.pack(anchor='w', padx=10, pady=5)    
    # Характеристика проводки (Радиокнопки)
    wiring_frame = ttk.Labelframe(frame_parameters, text="Материал проводки", relief=tk.RIDGE, borderwidth=1)
    wiring_frame.pack(fill='x', padx=10, pady=5)

    wiring_var = tk.StringVar()
    
    wiring_var.set(saved_data["Материал проводки"][1]) 
    wiring2 = ttk.Radiobutton(wiring_frame, text="Медь", variable=wiring_var, value="Медь")
    wiring2.pack(anchor='w', padx=20, pady=2)
    wiring2.bind("<ButtonRelease>", lambda e: update_saved_data("Материал проводки", wiring2))
    wiring1 = ttk.Radiobutton(wiring_frame, text="Алюминий", variable=wiring_var, value="Алюминий")
    wiring1.pack(anchor='w', padx=20, pady=2)
    wiring1.bind("<ButtonRelease>", lambda e: update_saved_data("Материал проводки", wiring1))

    # Количество проводников (Combobox)
    ttk.Label(frame_parameters, text="Количество проводников").pack(anchor='w', padx=3, pady=3)
    conductors = ttk.Combobox(frame_parameters, values=[
        "2-х жильный с одинарной изоляцией",
        "2-х проводной одинарным проводом",
        "2-х жильный с двойной изоляцией",
        "2-х жильный с дв. изол. моножила",
        "2-х жильный с дв. изол. гибкий",
        "3-х жильный с одинарной изоляцией",
        "3-х проводной одинарным проводом",
        "3-х жильный с дв. изол. моножила",
        "Кабель 2х моножила",
        "Кабель 2х гибкий",
        "Кабель 3х гибкий",
        "Кабель 3х +1х гибкий",
        "Провод СИП 2х",
        "Провод СИП 3х +",
        "Кабель гибкий контрольный",
        "Кабель сечением более 10мм2",
        "Кабель сечением более 25мм2",
        "Кабель сечением более 50мм2",
        "Слаботочка - сеть, телефон..."
    ], state="readonly")
    conductors.set(saved_data["Количество проводников"][1])
    conductors.pack(anchor='w', fill=tk.X, padx=10, pady=2)
    conductors.bind("<<ComboboxSelected>>", lambda e: update_saved_data("Количество проводников", conductors))

    # Тип монтажа (Combobox)
    ttk.Label(frame_parameters, text="Тип монтажа").pack(anchor='w', padx=3, pady=(3))
    mount_type = ttk.Combobox(frame_parameters, values=[
        "Открытый монтаж по стене",
        "Монтаж в штробе",
        "монтаж внутри каркаса для ГКЛ",
        "Монтаж по потолку",
        "Монтаж по полу"
    ], state="readonly")
    mount_type.set(saved_data["Тип монтажа"][1])
    mount_type.pack(anchor='w', fill=tk.X, padx=10, pady=2)
    mount_type.bind("<<ComboboxSelected>>", lambda e: update_saved_data("Тип монтажа", mount_type))

    # Варианты компоновки (Combobox)
    ttk.Label(frame_parameters, text="Варианты компоновки").pack(anchor='w', padx=3, pady=3)
    layout_options = ttk.Combobox(frame_parameters, values=[
        "Одна точка - один провод",
        "Одно помещение - одна РК",
        "Несколько помещений - одна РК",
        "Иное..."
    ], state="readonly")
    layout_options.set(saved_data["Варианты компоновки"][1])
    layout_options.pack(anchor='w', fill=tk.X, padx=10, pady=2)
    layout_options.bind("<<ComboboxSelected>>", lambda e: update_saved_data("Варианты компоновки", layout_options))

    return frame_parameters

# синхронизируем таблицу
# синхронизируем таблицу
def update_saved_data(name, widget):
    table_maneger = TableManager().update_saved_data
    table_maneger(name, widget)
