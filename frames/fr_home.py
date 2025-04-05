import tkinter as tk
from tkinter import ttk

def FrameHome(right_frame_home, saved_data):
    # Верхний фрейм управления
    control_frame = tk.Frame(right_frame_home, relief=tk.SUNKEN, borderwidth=1)
    control_frame.pack(side="top", fill=tk.X)
    ttk.Label(right_frame_home, text="Проектирование помещений").pack(padx=10, pady=2)
    
    # Основной фрейм для графики
    canvas = tk.Canvas(right_frame_home, bg='white')
    canvas.pack(fill=tk.BOTH, expand=True)

    # Фрейм для кнопок
    frame_buttons = ttk.Frame(right_frame_home, relief=tk.SUNKEN, borderwidth=1)
    frame_buttons.pack(fill=tk.X, side="bottom", padx=3, pady=3)

    # Кнопки
    btn_save = ttk.Button(frame_buttons, text="Сохранить", command=saved_frame)
    btn_save.pack(side="left", padx=5, pady=5)

    return right_frame_home

def saved_frame():
    print("Сохранить")
