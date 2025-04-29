# add_frames.py
from os import name
from tkinter import ttk
from functools import partial

from frames.fr_about import FrameAbout
from frames.fr_architecture import FrameArchitecture
from frames.fr_additional import FrameAdditional
from frames.fr_table import FrameTable
from frames.fr_geometry import FrameGeometry
from frames.fr_parameters import FrameParameters
from frames.fr_room_right import FrameRoomRight
from frames.fr_room_left import FrameRoomLeft
from frames.fr_home import FrameHome


class ContentFrame():
    def __init__(self, view, data, controller):
        self.view = view
        self.data = data
        self.controller = controller
        self.viget_frame = self.view.left_frame
        self.main_but_frame = self.view.main_but_frame
        self.right_frames = self.view
        self.frames = {}
        self.r_frames = {}
        # Загружаем данные из файла
        self.table_data = self.data.get_default_table()
        self.saved_data = self.data.get_default_settings()
    
        self.add_content_frame()
    def add_content_frame(self):

        # Загружаем все правые фреймы в память
        self.r_frames = {
            "Таблица": FrameTable(self.right_frames, self.table_data, self.saved_data, self.controller),
            "Помещение": FrameHome(self.right_frames, self.saved_data, self.controller),
            "Комната": FrameRoomRight(self.right_frames, self.saved_data, self.controller)            

        }
        # Загружаем все левые фреймы в память
        self.frames = {
             "Архитектура": FrameArchitecture(self.viget_frame, self.saved_data, self.controller),
            "Геометрия": FrameGeometry(self.viget_frame, self.saved_data, self.controller, self.r_frames),
            "Параметры Электро-оборудования": FrameParameters(self.viget_frame, self.saved_data, self.controller),
            "Дополнительно": FrameAdditional(self.viget_frame, self.saved_data, self.controller, self.r_frames),
            "О программе": FrameAbout(self.viget_frame, self.controller),
            "Комната": FrameRoomLeft(self.viget_frame, self.saved_data, self.controller)
            
            }
        
        for frame in self.frames.values():
            frame.grid_forget()
        
        # Упаковываем вкладки в основном окне и добавляем кнопки
        for key, frame in self.frames.items():
            if key != "Комната":
                btt = ttk.Button(self.main_but_frame, text=key, command=partial(self.show_frame, frame))
                btt.pack(fill='x', padx=1, pady=0)
        
        #frame=self.frames["О программе"]
        self.show_frame(self.frames["О программе"])
        return self.frames

    def show_frame(self, frame):
        for f in self.frames.values():
            f.grid_forget()        
        frame.grid(row=0, column=0, sticky="nsew")
        frame.focus_set()