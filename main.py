# main.py
import tkinter as tk
from tkinter import ttk

from data import DataManager
from view import AppView
from utils.add_frames import ContentFrame

class App:
    def __init__(self, root):
        # Инициализация главного окна
        self.root = root
        self.root.title("Дизайн Электрик")
        self.root.geometry("286x800")
        self.root.resizable(True, False)
        self.root.minsize(286, 800)
        self.root.style = ttk.Style()
        #self.root.style.theme_use("clam")
        self.data = DataManager()
        self.saved_data = {}

        
        # Инициализация интерфейса
        self.view = AppView(self.root, self)
        
        # Создание виджетов
        self.frames = ContentFrame(self.view, self.data, self)

    def show_right_frames(self, name):
        """ Отображает правый фрейм и обновляет состояние. """
        right_frame_instance=self.frames.r_frames[name]
        frame_text, frame_visible = self.saved_data.get("Правый фрейм", ["None", False])

        def show_frame():
            # Сначала скрываем все правые фреймы
            for frame in self.frames.r_frames.values():
                frame.pack_forget()

            right_frame_instance.pack(fill=tk.BOTH, expand=True)
            self.root.geometry("860x800")
            right_frame_instance.focus_set()
            self.saved_data["Правый фрейм"] = [name, True]

        def hide_frame():
            right_frame_instance.pack_forget()
            self.root.geometry("286x800")
            self.saved_data["Правый фрейм"] = [name, False]

        if frame_visible and frame_text == name:
            hide_frame()
        else:
            show_frame()


    def show_left_frames(self, name):
        print("show_left_frames")
        for f in self.frames.frames.values():
                f.grid_forget()

        f=self.frames.frames[name]
        f.grid(row=0, column=0, sticky="nsew")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    root.quit()
