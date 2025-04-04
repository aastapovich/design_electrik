# logic_app.py
import tkinter as tk
from tkinter import ttk

from functools import partial
from typing import Self

import utils.add_frames as add_frames


class LogicApp():
    GODFRAMES = {}
    def __init__(self, view):
        global VI
        VI = view

        self.view = view
        self.add_frames = add_frames.create_frames


    def add_content_frame(self, view):
        global GODFRAMES

        # Создаем словарь вкладок
        frames = self.add_frames(view.viget_frame, view.right_frames)
        GODFRAMES = frames

        # Упаковываем вкладки в основном окне и добавляем кнопки
        for key, frame in frames.items():
            if key == "Таблица" or key == "Комната":
                continue
            else:
                frame.grid(row=0, column=0, sticky="nsew")
                btt = ttk.Button(view.main_but_frame, text=key, command=partial(self.show_frame, frame))
                btt.pack(fill='x', padx=1, pady=0)

        return frames
    def show_frame(self, frame):
        frame.tkraise()

    def show_right_frames(text_frame):
        rt = VI
        frames = GODFRAMES

        # Изменить ширину основного окна и добавить правый фрейм frames[text_frame] в основное окно
        width = rt.winfo_width()
        if text_frame in frames:
            r_frame = frames[text_frame]
            if r_frame is not None:
                r_frame.grid()
                #r_frame.pack(fill=tk.BOTH, expand=True)
                if width is not None and width < 287:
                    print(type(rt))
                    rt.geometry("840x800")
                elif width >286:
                    rt.geometry("286x800")
