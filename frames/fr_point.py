import tkinter as tk
from tkinter import ttk

def FrameRoom(right_frames, saved_data):
    right_frame_room = right_frames.right_frame_room
    rect_lines = []  # Линии прямоугольника
    distributor = None  # Распределительная коробка
    traps = []  # Список точек
    rect = []  # Список соединительных линий
    points = []  # Список координат точек 
    
    ttk.Label(right_frame_room, text="Установка точек потребления").pack(anchor='w', padx=10, pady=2) 
    # Верхний фрейм управления
    control_frame = tk.Frame(right_frame_room, relief=tk.SUNKEN, borderwidth=1)
    control_frame.pack(side="top", fill=tk.X)
    
    
    # Основной фрейм для графики
    canvas = tk.Canvas(right_frame_room, bg='white')
    canvas.pack(fill=tk.BOTH, expand=True)

    # Фрейм для кнопок
    frame_buttons = ttk.Frame(right_frame_room, relief=tk.SUNKEN, borderwidth=1)
    frame_buttons.pack(fill=tk.X, side="bottom", padx=3, pady=3)
  
    # Кнопки
    btn_save = ttk.Button(frame_buttons, text="Сохранить", command=saved_frame)
    btn_save.pack(side="left", padx=5, pady=5)
    btn_new = ttk.Button(frame_buttons, text="Очистить", command=new_frame)
    btn_new.pack(side="left", padx=5, pady=5)
    btn_cancel = ttk.Button(frame_buttons, text="Выход", command=exit_frame)
    btn_cancel.pack(side="left", padx=5, pady=5)

    return right_frame_room
    
def saved_frame():
    print("Сохранить")

def new_frame():
    print("Очистить")

def exit_frame():
    print("Выход")
