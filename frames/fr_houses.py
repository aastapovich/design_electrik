import tkinter as tk
from tkinter import ttk
from logic_table import TableManager

def FrameHouse(parent, table_data, saved_data):
    # Основной фрейм для таблицы
    frame_house = ttk.Frame(parent, relief=tk.SUNKEN, borderwidth=1)
    frame_house.grid(row=0, column=2, sticky='nsew')


    frame_table_viev = ttk.Frame(frame_house, relief=tk.SUNKEN, borderwidth=1)
    frame_table_viev.pack(fill=tk.BOTH, expand=True)
    # Фрейм для кнопок
    frame_table_buttons = ttk.Frame(frame_house, relief=tk.SUNKEN, borderwidth=1)
    frame_table_buttons.pack(fill=tk.X, expand=False, pady=3)

    return frame_house

# синхронизируем таблицу
def update_saved_data(name, widget):
    table_maneger = TableManager().update_saved_data
    table_maneger(name, widget)

def update_saved_check(name, widget):
    table_maneger = TableManager().update_saved_check
    table_maneger(name, widget)
