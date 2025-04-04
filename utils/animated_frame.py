import tkinter as tk
from tkinter import ttk

class AnimatedFrame(ttk.Frame):
    """Универсальный класс анимации виджетов в Tkinter."""
    
    def __init__(self, parent, animation="fade", direction="left", speed=30, steps=20, **kwargs):
        """
        :param parent: Родительский виджет
        :param animation: Тип анимации ('fade', 'slide', 'zoom', 'blink')
        :param direction: Направление ('left', 'right', 'top', 'bottom') - для slide и zoom
        :param speed: Задержка между кадрами (мс)
        :param steps: Количество шагов анимации
        """
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.animation = animation
        self.direction = direction
        self.speed = speed
        self.steps = steps
        self.step = 0  # Счётчик текущего кадра

        # Начальная конфигурация
        if animation == "fade":
            self.alpha = 0
            self.parent.attributes("-alpha", 0)  # Начальная прозрачность окна
        elif animation == "slide":
            self.init_slide_position()
        elif animation == "zoom":
            self.init_zoom_position()

        self.place(x=50, y=50, width=300, height=200)  # Начальная позиция

        # Запуск анимации
        self.animate()

    def init_slide_position(self):
        """Устанавливает начальную позицию для slide анимации."""
        w, h = 300, 200  # Размер фрейма
        if self.direction == "left":
            self.place(x=-w, y=50, width=w, height=h)
        elif self.direction == "right":
            self.place(x=500, y=50, width=w, height=h)
        elif self.direction == "top":
            self.place(x=50, y=-h, width=w, height=h)
        elif self.direction == "bottom":
            self.place(x=50, y=300, width=w, height=h)

    def init_zoom_position(self):
        """Устанавливает начальный масштаб для zoom анимации."""
        self.scale_factor = 0.1
        self.place(x=50, y=50, width=300 * self.scale_factor, height=200 * self.scale_factor)

    def animate(self):
        """Запускает выбранную анимацию."""
        if self.animation == "fade":
            self.fade_in()
        elif self.animation == "slide":
            self.slide_in()
        elif self.animation == "zoom":
            self.zoom_in()
        elif self.animation == "blink":
            self.blink()

    def fade_in(self):
        """Анимация плавного появления."""
        if self.step < self.steps:
            self.alpha += 1 / self.steps
            self.parent.attributes("-alpha", self.alpha)
            self.step += 1
            self.after(self.speed, self.fade_in)

    def slide_in(self):
        """Анимация выезда (slide) с указанного направления."""
        if self.step < self.steps:
            dx = 300 // self.steps  # Шаг движения по X
            dy = 200 // self.steps  # Шаг движения по Y
            x = self.place_info()["x"]
            y = self.place_info()["y"]
            x, y = int(x), int(y)

            if self.direction == "left":
                self.place(x=x + dx)
            elif self.direction == "right":
                self.place(x=x - dx)
            elif self.direction == "top":
                self.place(y=y + dy)
            elif self.direction == "bottom":
                self.place(y=y - dy)

            self.step += 1
            self.after(self.speed, self.slide_in)

    def zoom_in(self):
        """Анимация увеличения масштаба."""
        if self.step < self.steps:
            self.scale_factor += (1 - 0.1) / self.steps
            new_width = int(300 * self.scale_factor)
            new_height = int(200 * self.scale_factor)
            self.place(width=new_width, height=new_height)
            self.step += 1
            self.after(self.speed, self.zoom_in)

    def blink(self):
        """Анимация мигания (виджет исчезает и появляется)."""
        if self.step < self.steps:
            self.step += 1
            self.place_forget() if self.step % 2 == 0 else self.place(x=50, y=50, width=300, height=200)
            self.after(self.speed, self.blink)

# === Тестирование ===
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x300")

    # Создание анимированного фрейма (изменяйте параметры для теста)
    frame = AnimatedFrame(root, animation="slide", direction="top", speed=20, steps=30)
    ttk.Label(frame, text="Анимированный фрейм", font=("Arial", 14)).pack(pady=20)

    root.mainloop()
