# view.py

import tkinter as tk
from tkinter import ttk


class AppView():
    def __init__(self, root):
        self.root = root
        
        # Основной фрейм с двумя колонками: левая – для вкладок Виджетов, правая – для таблицы
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=0)
        self.main_frame.columnconfigure(1, weight=2)
        self.main_frame.rowconfigure(0, weight=1)

        # Левый фрейм для Виджетов (SUNKEN, RAISED, GROOVE, RIDGE) - тип границы фрейма
        self.viget_frame = ttk.Frame(self.main_frame, width=270, relief=tk.SUNKEN, borderwidth=1)
        self.viget_frame.grid(row=0, column=0, sticky="nsew", padx=3, pady=3)

        # Нижний фрейм для рабочих кнопок
        self.main_but_frame = ttk.Frame(self.viget_frame)
        self.main_but_frame.grid(row=1, column=0, sticky="nsew", padx=3, pady=3)#.pack(fill='x')

        # Фрейм для нижних кнопок левого фрейма
        self.button_frame_left = ttk.Frame(self.viget_frame, relief=tk.SUNKEN, borderwidth=1)
        self.button_frame_left.grid(row=2, column=0, sticky="nsew", padx=3, pady=3)

        # Нижние кнопки левого фрейма
        btn_cancel = ttk.Button(self.button_frame_left, text="Выход", command=self.quit)
        btn_apply = ttk.Button(self.button_frame_left, text="Сохранить", command=self.on_save)
        btn_cancel.pack(side='left', expand=True, padx=3, pady=3)
        btn_apply.pack(side='right', expand=True, padx=3, pady=3)


        # Фрейм для содержимого правого фрейма
        self.right_frames = ttk.Frame(self.main_frame, relief=tk.SUNKEN, borderwidth=1)
        self.right_frames.grid(row=0, column=1, sticky="nsew", padx=3, pady=3)



    # Обработка нажатия кнопки "Применить"
    def on_save(self):
        print(type(self.frames))

    # Обработка нажатия кнопки "Выход"
    def quit(self):
        self.root.quit()

