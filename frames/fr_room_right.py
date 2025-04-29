import tkinter as tk
from tkinter import ttk


def FrameRoomRight(right_frames, saved_data, controller):
    
    right_frame_room = right_frames.right_frame_room

    # Основной фрейм для графики
    canvas = tk.Canvas(right_frame_room, bg='white')
    canvas.pack(fill=tk.BOTH, expand=True)

    # Фрейм для кнопок
    frame_buttons = ttk.Frame(right_frame_room, relief=tk.SUNKEN, borderwidth=1)
    frame_buttons.pack(fill=tk.X, side="bottom", padx=3, pady=3)
  
    # Кнопки
    btn_open = ttk.Button(frame_buttons, text="Открыть", command=open_project)
    btn_open.pack(side="left", padx=5, pady=5)
    btn_new = ttk.Button(frame_buttons, text="Очистить", command=new_frame)
    btn_new.pack(side="left", padx=5, pady=5)
    btn_save = ttk.Button(frame_buttons, text="Сохранить", command=saved_frame)
    btn_save.pack(side="left", padx=5, pady=5)
    btn_cancel = ttk.Button(frame_buttons, text="Выход", command=exit_frame)
    btn_cancel.pack(side="left", padx=5, pady=5)

    return right_frame_room


def saved_frame():
    print("Сохранить")

def new_frame():
    print("Очистить")

def exit_frame():
    print("Выход")

def open_project():
    print("Открыть")