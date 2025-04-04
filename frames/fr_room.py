import tkinter as tk
from tkinter import ttk

def FrameRoom(right_frames, saved_data):
    rect_lines = []  # Линии прямоугольника
    distributor = None  # Распределительная коробка
    traps = []  # Список точек
    rect = []  # Список соединительных линий
    points = []  # Список координат точек 
    
    # Верхний фрейм управления
    control_frame = tk.Frame(right_frames, width=600, height=800, bg='gray')
    control_frame.pack(side="top", fill=tk.X)
    
    # Основной фрейм для графики
    canvas = tk.Canvas(right_frames, bg='white')
    canvas.pack(fill=tk.BOTH, expand=True)

    # Фрейм для кнопок
    frame_buttons = ttk.Frame(right_frames, relief=tk.SUNKEN, borderwidth=1)
    frame_buttons.pack(fill=tk.X, side="bottom", padx=3, pady=3)
  
    # Кнопки
    btn_save = ttk.Button(frame_buttons, text="Сохранить", command=saved_frame)
    btn_save.pack(side="left", padx=5, pady=5)
    btn_new = ttk.Button(frame_buttons, text="Очистить", command=new_frame)
    btn_new.pack(side="left", padx=5, pady=5)
    btn_cancel = ttk.Button(frame_buttons, text="Выход", command=exit_frame)
    btn_cancel.pack(side="left", padx=5, pady=5)

    return right_frames
    
def saved_frame():
    print("Сохранить")

def new_frame():
    print("Очистить")

def exit_frame():
    print("Выход")



# def on_apply_table(self):
#     table_manager.fill_table(table_data, saved_data)
