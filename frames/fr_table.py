import tkinter as tk
from tkinter import ttk
from logic_table import TableManager


table_manager = TableManager()
def FrameTable(right_frames, table_data, saved_data):

    # Фрейм для названия таблицы
    frame_label = tk.Label(right_frames, relief=tk.SUNKEN, borderwidth=1, text="Сводная таблица параметров", font=("Arial", 14, "bold"))
    frame_label.pack(fill=tk.X, side="top", padx=3, pady=3)
 
    # Фрейм для таблицы
    columns = ("name", "quantity", "unit")
    st_table = ttk.Treeview(right_frames, columns=columns, show="headings")
    st_table.heading("name", text="Наименование")
    st_table.heading("quantity", text="Значение")
    st_table.heading("unit", text="ед. изм")
    st_table.column("name", width=160)
    st_table.column("quantity", width=220)
    st_table.column("unit", width=45)
    st_table.tag_configure("disabled", foreground='gray')
    st_table.tag_configure("default", foreground='black')
    st_table.pack(fill=tk.BOTH, expand=True)

    table_manager = TableManager(st_table)
    st_table.bind("<Double-1>", lambda event: table_manager.on_row_clicks(event, table_data, saved_data))

    # Фрейм для кнопок
    frame_table_buttons = ttk.Frame(right_frames, relief=tk.SUNKEN, borderwidth=1)
    frame_table_buttons.pack(fill=tk.X, side="bottom", padx=3, pady=3)
    
    # Кнопки
    btn_cancel_table = ttk.Button(frame_table_buttons, text="Восстановить таблицу", command=lambda: table_manager.default_apply_table(table_data, saved_data))
    btn_apply_table = ttk.Button(frame_table_buttons, text="Скрыть выделенные строки", command=lambda: table_manager.fill_table(table_data, saved_data))
    btn_cancel_table.pack(side="left", padx=3, pady=3)
    btn_apply_table.pack(side="left", padx=3, pady=3)

    # Заполнение таблицы
    table_manager.fill_table(table_data, saved_data)

    return right_frames