import tkinter as tk
from tkinter import ttk
from logic.logic_table import TableManager


table_manager = TableManager()
import tkinter as tk
from tkinter import ttk

def FrameTable(right_frames, table_data, saved_data, controller):
    right_frame_table = right_frames.right_frame_table

    # Название таблицы
    label = ttk.Label(right_frame_table, text="Сводная таблица параметров", font=("Arial", 14, "bold"))
    label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

    # Фрейм для таблицы и скроллбара
    frame_table = ttk.Frame(right_frame_table)
    frame_table.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

    columns = ("name", "quantity", "unit")
    st_table = ttk.Treeview(frame_table, columns=columns, show="headings")
    st_table.heading("name", text="Наименование")
    st_table.heading("quantity", text="Значение")
    st_table.heading("unit", text="ед. изм")
    st_table.column("name", width=160)
    st_table.column("quantity", width=220)
    st_table.column("unit", width=45)
    st_table.tag_configure("disabled", foreground='gray')
    st_table.tag_configure("default", foreground='black')

    # Создаём вертикальный скроллбар
    scrollbar = ttk.Scrollbar(frame_table, orient="vertical", command=st_table.yview)
    st_table.configure(yscrollcommand=lambda f, l: on_scrollbar(f, l, scrollbar))

    # Размещение таблицы и скроллбара
    st_table.grid(row=0, column=0, sticky="nsew")
    scrollbar.grid(row=0, column=1, sticky="ns")

    # Настройка веса строк и столбцов для растягивания
    frame_table.grid_rowconfigure(0, weight=1)
    frame_table.grid_columnconfigure(0, weight=1)

    table_manager = TableManager(st_table)
    st_table.bind("<Double-1>", lambda event: table_manager.on_row_clicks(event, table_data, saved_data))

    # Фрейм для кнопок
    frame_table_buttons = ttk.Frame(right_frame_table, relief=tk.SUNKEN, borderwidth=1)
    frame_table_buttons.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

    # Кнопки
    btn_cancel_table = ttk.Button(frame_table_buttons, text="Восстановить таблицу", command=lambda: table_manager.default_apply_table(table_data, saved_data))
    btn_apply_table = ttk.Button(frame_table_buttons, text="Скрыть выделенные строки", command=lambda: table_manager.fill_table(table_data, saved_data))
    btn_cancel_table.grid(row=0, column=0, padx=3, pady=3, sticky="w")
    btn_apply_table.grid(row=0, column=1, padx=3, pady=3, sticky="w")

    # Настройка веса основного фрейма
    right_frame_table.grid_rowconfigure(1, weight=1)
    right_frame_table.grid_columnconfigure(0, weight=1)

    # Заполнение таблицы
    table_manager.fill_table(table_data, saved_data)

    return right_frame_table

# Вспомогательная функция для автоскрытия скроллбара
def on_scrollbar(first, last, scrollbar):
    if float(first) <= 0.0 and float(last) >= 1.0:
        scrollbar.grid_remove()  # Скрыть скроллбар, если не нужен
    else:
        scrollbar.grid()  # Показать скроллбар
    scrollbar.set(first, last)


