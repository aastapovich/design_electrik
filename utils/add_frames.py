# add_frames.py
from data import DataManager 
from frames.fr_about import FrameAbout
from frames.fr_architecture import FrameArchitecture
from frames.fr_additional import FrameAdditional
from frames.fr_table import FrameTable
from frames.fr_geometry import FrameGeometry
from frames.fr_parameters import FrameParameters
from frames.fr_room import FrameRoom

my_date = DataManager()
saved_data = my_date.get_default_settings()
table_data = my_date.get_default_table()

def create_frames(viget_frame, right_frame):
# Загружаем все фреймы в память
    frames = {
        "Архитектура": FrameArchitecture(viget_frame, saved_data),
        "Геометрия": FrameGeometry(viget_frame, saved_data),
        "Параметры Электро-оборудования": FrameParameters(viget_frame, saved_data),
        "Дополнительно": FrameAdditional(viget_frame, saved_data),
        "О программе": FrameAbout(viget_frame),
        "Таблица": FrameTable(right_frame, table_data, saved_data),
        "Комната": FrameRoom(right_frame, saved_data)
    }

    return frames
