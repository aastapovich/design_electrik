# fr_geometry.py
import tkinter as tk
from tkinter import ttk

from logic.logic_table import TableManager

def FrameGeometry(parent, saved_data, controller, r_frames):
    """ Фрейм с геометрией. """

    frame_geometry = ttk.Frame(parent)

    # Заголовок панели
    lbl_title = ttk.Label(frame_geometry, text="Геометрия", font=("Arial", 14, "bold"))
    lbl_title.pack(anchor='w', padx=10, pady=5)
    var0 = tk.IntVar() # Переменная для чекбокса Добавить комнату
    var1 = tk.IntVar() # Переменная для чекбокса Добавить промышленное помещение
    var2 = tk.IntVar() # Переменная для чекбокса Добавить подвальный этаж
    var3 = tk.IntVar() # Переменная для чекбокса Добавить технологический этаж
  
    but_plan = ttk.Button(frame_geometry, text="Выбрать готовую планировку", command=lambda: show_frame(controller, "Помещение"))
    but_plan.pack(anchor='w', padx=10, pady=5)
   

    var = ttk.Checkbutton(frame_geometry, text="Добавить комнату", onvalue=1,
                    offvalue=0, variable=var0)
    var.pack(anchor='w', padx=10, pady=2)
    var.bind("<ButtonRelease>", lambda e: update_saved_check("Добавить комнату", var0))

    ttk.Label(frame_geometry, text="Длина помещения").pack(anchor='w', padx=10, pady=2)
    length = ttk.Spinbox(frame_geometry, from_=1, to=100, increment=0.1, width=5)
    length.set(saved_data["Длина помещения"][1])
    length.pack(anchor='w', padx=20)
    length.bind("<ButtonRelease>", lambda e: update_saved_data("Длина помещения", length))
    
    ttk.Label(frame_geometry, text="Ширина помещения").pack(anchor='w', padx=10, pady=2)
    width = ttk.Spinbox(frame_geometry, from_=1, to=100, increment=0.1, width=5)
    width.set(saved_data["Ширина помещения"][1])
    width.pack(anchor='w', padx=20)
    width.bind("<ButtonRelease>", lambda e: update_saved_data("Ширина помещения", width))

    but = ttk.Button(frame_geometry, text="Редактировать в отдельном окне", command=lambda: show_frame(controller, "Комната"))
    but.pack(anchor='w', padx=10, pady=5)
    
    add_basement = ttk.Checkbutton(frame_geometry, text="Добавить подвальный этаж", variable=var2)
    var2.set(saved_data["Добавить подвальный этаж"][1])
    add_basement.pack(anchor='w', padx=10, pady=2)
    add_basement.bind("<ButtonRelease>", lambda e: update_saved_check("Добавить подвальный этаж", var2))
    
    add_tech_floor = ttk.Checkbutton(frame_geometry, text="Добавить технологический этаж", variable=var3)
    var3.set(saved_data["Добавить технологический этаж"][1])
    add_tech_floor.pack(anchor='w', padx=10, pady=2)
    add_tech_floor.bind("<ButtonRelease>", lambda e: update_saved_check(
                                    "Добавить технологический этаж", var3))
    
    # пропуск строки
    ttk.Label(frame_geometry, text="").pack(anchor='w', padx=10, pady=2)

    add_pro = ttk.Checkbutton(frame_geometry, text="Промышленное здание", variable=var1)
    var1.set(saved_data["Промышленное здание"][1])
    add_pro.pack(anchor='w', padx=10, pady=2)
    add_pro.bind("<ButtonRelease>", lambda e: update_saved_check("Промышленное здание", var1))


    ttk.Label(frame_geometry, text="Промышленное здание(тип)").pack(anchor='w', padx=10, pady=2)
    building = ttk.Combobox(frame_geometry, values=[
        "Ангар из стальных конструкций",
        "Ангар из Ж/Б конструкций",
        "Бокс",
        "Ферма из Ж/Б конструкций",
        "Сложное пром. сооружение",
        "Другое..."
    ])
    building.set(saved_data["Промышленное здание(тип)"][1])
    building.pack(anchor='w', fill=tk.X, padx=10, pady=2)
    building.bind("<<ComboboxSelected>>", lambda e: update_saved_data("Промышленное здание(тип)", building))
    
    ttk.Label(frame_geometry, text="Длина здания").pack(anchor='w', padx=10, pady=2)
    building_length = ttk.Spinbox(frame_geometry, from_=1, to=100, increment=0.1, width=5)
    building_length.set(saved_data["Длина здания"][1])
    building_length.pack(anchor='w', padx=20)
    building_length.bind("<ButtonRelease>", lambda e: update_saved_data("Длина здания", building_length))
    
    ttk.Label(frame_geometry, text="Ширина здания").pack(anchor='w', padx=10, pady=2)
    building_width = ttk.Spinbox(frame_geometry, from_=1, to=100, increment=0.1, width=5)
    building_width.set(saved_data["Ширина здания"][1])
    building_width.pack(anchor='w', padx=20)
    building_width.bind("<ButtonRelease>", lambda e: update_saved_data("Ширина здания", building_width))
    
    ttk.Label(frame_geometry, text="Высота здания").pack(anchor='w', padx=10, pady=2)
    building_height = ttk.Spinbox(frame_geometry, from_=1, to=50, increment=0.1, width=5)
    building_height.set(saved_data["Высота здания"][1])
    building_height.pack(anchor='w', padx=20)
    building_height.bind("<ButtonRelease>", lambda e: update_saved_data("Высота здания", building_height))

    return frame_geometry

# синхронизируем таблицу
def update_saved_data(name, widget):
    table_maneger = TableManager().update_saved_data
    table_maneger(name, widget)

def update_saved_check(name, widget):
    table_maneger = TableManager().update_saved_check
    table_maneger(name, widget)

def show_frame(controller, name):
    if name == "Комната":
        controller.show_right_frames(name)
        controller.show_left_frames(name)
    elif name == "Помещение":
        controller.show_right_frames(name)
    else:
        pass
        
    