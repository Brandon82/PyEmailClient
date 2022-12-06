from helpers import *
import dearpygui.dearpygui as dpg

class FontManager:
    def __init__(self, file_path: str):
        self.file_path: str = file_path
        with dpg.font_registry():
            if platform == 'darwin':
                self.h1_b = dpg.add_font((self.file_path) + '/Fonts/OpenSans-Bold.ttf', 34)
                self.h2_b = dpg.add_font((self.file_path) + '/Fonts/OpenSans-Bold.ttf', 22)

                self.b2 = dpg.add_font((self.file_path) + '/Fonts/OpenSans-Regular.ttf', 22)
                self.b2_sb = dpg.add_font((self.file_path) + '/Fonts/OpenSans-Regular.ttf', 22)

            elif platform == 'win32':
                self.h1_b = dpg.add_font((self.file_path) + '\Fonts\OpenSans-Bold.ttf', 34)
                self.h2_b = dpg.add_font((self.file_path) + '\Fonts\OpenSans-Bold.ttf', 22)

                self.b2 = dpg.add_font((self.file_path) + '\Fonts\OpenSans-Regular.ttf', 22)
                self.b2_sb = dpg.add_font((self.file_path) + '\Fonts\OpenSans-SemiBold.ttf', 22)