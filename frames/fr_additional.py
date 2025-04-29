# fr_additional.py
import tkinter as tk
from tkinter import ttk

from logic.logic_table import TableManager

def FrameAdditional(parent, saved_data, controller, r_frames):
    """ Фрейм с Дополнительными настройками. """

    frame_additional = ttk.Frame(parent)

    # Заголовок панели
    lbl_title = ttk.Label(frame_additional, text="Дополнительно", font=("Arial", 14, "bold"))
    lbl_title.pack(anchor='w', padx=10, pady=5)

    # Тема  интерфейса
    ttk.Label(frame_additional, text="Тема интерфейса").pack(anchor='w', padx=10, pady=2)
    cmb_theme = ttk.Combobox(frame_additional, state="readonly", values=["Светлая тема", "Серая тема", "Тёмная тема"])
    cmb_theme.set(saved_data["Тема интерфейса"][1])
    cmb_theme.pack(anchor='w', fill=tk.X, padx=20, pady=2)
    cmb_theme.bind("<<ComboboxSelected>>", lambda e: update_saved_data("Тема интерфейса", cmb_theme))

    # Шрифты
    ttk.Label(frame_additional, text="Шрифт").pack(anchor='w', padx=10, pady=2)
    cmb_font = ttk.Combobox(frame_additional, state="readonly", values=[
        "Arial", "Times New Roman", "Courier New", "Comic Sans MS",
        "Verdana", "Tahoma", "Georgia", "Impact", "Lucida Console"
    ])
    cmb_font.set(saved_data["Шрифт"][1])
    cmb_font.pack(anchor='w', fill=tk.X, padx=20, pady=2)
    cmb_font.bind("<<ComboboxSelected>>", lambda e: update_saved_data("Шрифт", cmb_font))

    # Размер шрифта
    ttk.Label(frame_additional, text="Размер шрифта").pack(anchor='w', padx=10, pady=2)
    spn_font_size = ttk.Spinbox(frame_additional, from_=11, to=18, width=5)
    spn_font_size.set(saved_data["Размер шрифта"][1])
    spn_font_size.pack(anchor='w', padx=20, pady=2)
    spn_font_size.bind("<ButtonRelease>", lambda e: update_saved_data("Размер шрифта", spn_font_size))


    # Кнопка применения настроек
    btn_apply = ttk.Button(frame_additional, text="Изменить", command=apply_settings)
    btn_apply.pack(anchor='w', padx=20, pady=10)
    # Кнопка изменения таблицы
    btn_apply = ttk.Button(frame_additional, text="Таблица", command=lambda: controller.show_right_frames("Таблица"))
    btn_apply.pack(anchor='w', padx=20, pady=10)

    return frame_additional

def apply_settings():
    print("Тема интерфейса изменена")

# синхронизируем таблицу
def update_saved_data(name, widget):
    table_maneger = TableManager().update_saved_data
    table_maneger(name, widget)

def update_saved_check(name, widget):
    table_maneger = TableManager().update_saved_check
    table_maneger(name, widget)
