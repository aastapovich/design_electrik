# view.py

import tkinter as tk
from tkinter import ttk


class AppView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)        
        self.controller = controller
        self.parent = parent

        """ Создание интерфейса главного окна программы. """        
        # Основной фрейм с двумя колонками: левая – для вкладок Виджетов, правая – для таблицы

  
        # Левый фрейм для Виджетов
        self.left_frame = ttk.Frame(self.parent, width=280)
        self.left_frame.grid(row=0, column=0, sticky="ns", padx=3, pady=3)
        # Фрейм для правого окна
        self.right_frame = ttk.Frame(self.parent)
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=3, pady=3)
        # Настройка растяжения фреймов
        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(1, weight=1)


        self.viget_frame = ttk.Frame(self.left_frame)
        self.viget_frame.grid(row=0, column=0, sticky="nsew", padx=3, pady=3)

        self.left_frame.grid_rowconfigure(0, weight=1)  # Верхний фрейм растягивается
        self.left_frame.grid_rowconfigure(1, weight=0)  # Средний фрейм фиксирован
        self.left_frame.grid_rowconfigure(2, weight=0)  # Нижний фрейм фиксирован
        self.left_frame.grid_columnconfigure(0, weight=1)  # Фиксируем ширину левого фрейма     
        
        # Нижний фрейм для рабочих кнопок
        self.main_but_frame = ttk.Frame(self.left_frame)
        self.main_but_frame.grid(row=1, column=0, sticky="ew", padx=3, pady=3)

        # Фрейм для нижних кнопок левого фрейма
        self.button_frame_left = ttk.Frame(self.left_frame, relief=tk.SUNKEN, borderwidth=1)
        self.button_frame_left.grid(row=2, column=0, sticky="ew", padx=3, pady=3)


        # Нижние кнопки левого фрейма
        btn_cancel = ttk.Button(self.button_frame_left, text="Выход", command=self.quit)
        btn_apply = ttk.Button(self.button_frame_left, text="Сохранить", command=self.on_save)
        btn_cancel.grid(row=0, column=0, sticky='ew')
        btn_apply.grid(row=0, column=1, sticky='ew')
        
        self.button_frame_left.grid_columnconfigure(0, weight=1)
        self.button_frame_left.grid_columnconfigure(1, weight=1)
        
        # Фрейм для таблицы правого фрейма
        self.right_frame_table = ttk.Frame(self.right_frame, relief=tk.SUNKEN, borderwidth=1)
        # Фрейм для комнат правого фрейма
        self.right_frame_room = ttk.Frame(self.right_frame, relief=tk.SUNKEN, borderwidth=1)
        # Фрейм для домов правого фрейма
        self.right_frame_home = ttk.Frame(self.right_frame, relief=tk.SUNKEN, borderwidth=1)
     

    # Обработка нажатия кнопки "Сохранить"
    def on_save(self):
        print("Сохранить")

    # Обработка нажатия кнопки "Выход"
    def quit(self):
        print("Выход")
        self.controller.root.quit()

