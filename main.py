# main.py
import tkinter as tk
from tkinter import ttk

from view import AppView
from logic_app import LogicApp


class App:
    def __init__(self, root):

        super().__init__()
        self.root = root
        self.root.title("Дизайн Электрик")
        self.root.geometry("286x800")
        self.root.resizable(True, False)
        self.root.minsize(286, 800)
        self.root.style = ttk.Style()
        #self.root.style.theme_use("clam")


        self.logic = LogicApp(root)
        # Инициализация интерфейса
        self.view = AppView(root)

        # Добавление контентных фреймов
        self.frames = self.logic.add_content_frame(self.view)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    root.quit()
