"""
frames/fr_architecture.py
Фрейм "Архитектура".
"""

import tkinter as tk
from tkinter import ttk

from logic.logic_table import TableManager

def FrameArchitecture(parent, saved_data, controller):
    """ Фрейм с архитектурными данными. """ 
    frame_arhitecture = ttk.Frame(parent)

    """ Создание интерфейса фрейма. """
    lbl_title = ttk.Label(frame_arhitecture, text="Архитектура")
    lbl_title.pack(anchor='w', padx=10, pady=5)
     # Тип строения
    ttk.Label(frame_arhitecture, text="Тип строения").pack(anchor='w', padx=10, pady=2)
    home_type = ttk.Combobox(frame_arhitecture, values=["Квартира", "Промышленное сооружение",
                                                    "Частный дом", "Гараж", "Подсобное сооружение", "Деревянный стуб"])
    home_type.set(saved_data["Тип строения"][1])
    home_type.pack(anchor='w', fill=tk.X, padx=20)
    home_type.bind("<<ComboboxSelected>>", lambda e: update_saved_data("Тип строения", home_type))

    # Количество комнат
    ttk.Label(frame_arhitecture, text="Количество комнат").pack(anchor='w', padx=10, pady=2)
    rooms = ttk.Spinbox(frame_arhitecture, from_=1, to=99, increment=1, width=5)
    rooms.set(saved_data["Количество комнат"][1])
    rooms.pack(anchor='w', padx=20)
    rooms.bind("<ButtonRelease>", lambda e: update_saved_data("Количество комнат", rooms))

    # Количество этажей
    ttk.Label(frame_arhitecture, text="Количество этажей").pack(anchor='w', padx=10, pady=2)
    floors = ttk.Spinbox(frame_arhitecture, from_=1, to=99, increment=1, width=5)
    floors.set(saved_data["Количество этажей"][1])
    floors.pack(anchor='w', padx=20)
    floors.bind("<ButtonRelease>", lambda e: update_saved_data("Количество этажей", floors))

    # Материал стен
    ttk.Label(frame_arhitecture, text="Материал стен").pack(anchor='w', padx=10, pady=2)
    wall_material = ttk.Combobox(frame_arhitecture, values=[
                                                    "Кирпич красный полнотелый",
                                                    "Кирпич красный пустотелый",
                                                    "Кирпич силикатный", "Ж/Бетон",
                                                    "Пеноблок","Фиброплита", "Дерево"])
    wall_material.set(saved_data["Материал стен"][1])
    wall_material.pack(anchor='w', fill=tk.X, padx=20)
    wall_material.bind("<<ComboboxSelected>>", lambda e: update_saved_data("Материал стен", wall_material))

    # Отделка стен
    ttk.Label(frame_arhitecture, text="Отделка стен").pack(anchor='w', padx=10, pady=2)
    wall_finish = ttk.Combobox(frame_arhitecture, values=["Штукатурка цементная", "Шпаклевка гипсовая", "ГКЛ, ОСП, панели", "Без отделки"])
    wall_finish.set(saved_data["Отделка стен"][1])
    wall_finish.pack(anchor='w', fill=tk.X, padx=20)
    wall_finish.bind("<<ComboboxSelected>>", lambda e: update_saved_data("Отделка стен", wall_finish))

    # Материал потолка
    ttk.Label(frame_arhitecture, text="Материал потолка").pack(anchor='w', padx=10, pady=2)
    ceiling_material = ttk.Combobox(frame_arhitecture, values=[
        "Ж/Б Пустотная плита", "Ж/Бетон монолит", "Дерево"
        ])
    ceiling_material.set(saved_data["Материал потолка"][1])
    ceiling_material.pack(anchor='w', fill=tk.X, padx=20)
    ceiling_material.bind("<<ComboboxSelected>>", lambda e: update_saved_data("Материал потолка", ceiling_material))

    # Высота потолка
    ttk.Label(frame_arhitecture, text="Высота потолка(м)").pack(anchor='w', padx=10, pady=2)
    ceiling_height = ttk.Spinbox(frame_arhitecture, from_=1, to=99, increment=0.05, width=5)
    ceiling_height.set(saved_data["Высота потолка"][1])
    ceiling_height.pack(anchor='w', padx=20)
    ceiling_height.bind("<ButtonRelease>", lambda e: update_saved_data("Высота потолка", ceiling_height))

    # Финишная отделка потолка
    ttk.Label(frame_arhitecture, text="Финишная отделка потолка").pack(anchor='w', padx=10, pady=2)
    ceiling_finish = ttk.Combobox(frame_arhitecture, values=[
        "ПВХ натяжной или тканевый", "Гипсокартон по профилю",
        "Дерево, ОСП по брускам", "Шпаклевка, покраска", "Без отделки"
        ])
    ceiling_finish.set(saved_data["Финишная отделка потолка"][1])
    ceiling_finish.pack(anchor='w', fill=tk.X, padx=20)
    ceiling_finish.bind("<<ComboboxSelected>>", lambda e: update_saved_data("Финишная отделка потолка", ceiling_finish))

    return frame_arhitecture

# синхронизируем таблицу
# синхронизируем таблицу
def update_saved_data(name, widget):
    table_maneger = TableManager().update_saved_data
    table_maneger(name, widget)
