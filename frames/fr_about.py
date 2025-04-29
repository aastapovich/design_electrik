# fr_about.py
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

""" 
frames/fr_about.py
Фрейм "О программе".
"""
bg_image = None

def FrameAbout(parent, controller):
    """ Фрейм с информацией о программе. """
    global bg_image  # Объявляем bg_image как глобальную переменную
    about_text = "Дизайн Электрик" \
        "\nВерсия 1.0\n\n" \
        "Программа для проектирования\n" \
        "электрических сетей\n" \
        "гражданских и промышленных\n" \
        "объектов.\n"
    frame_about = ttk.Frame(parent)

    
    if not bg_image:
        bg_image = load_image()  # Загружаем изображение, если оно еще не загружено

    if bg_image:
        ttk.Label(frame_about, image=bg_image, relief="flat").grid(row=0, column=0, sticky='nsew')  # Используем grid для размещения
    else:
        ttk.Label(frame_about, text=about_text).grid(row=0, column=0, sticky='nsew')  # Если изображения нет, выводим текст

    return frame_about


# Загрузка изображения
def load_image():
    try:
        # Пробуем загрузить изображение с корректной обработкой ошибок
        image = Image.open("img/Titul.png")  # Убедитесь, что путь правильный!
        image = image.resize((274, 600), Image.LANCZOS)  # Изменение размера для нормальной загрузки
        bg_image = ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Ошибка загрузки изображения: {e}")
        bg_image = None
    return bg_image
