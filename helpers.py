import dearpygui.dearpygui as dpg
from sys import platform
import os

def get_platform():
    return platform

def get_file_path():
    return os.path.dirname(os.path.realpath(__file__))

class LayoutHelper:
    def __init__(self):
        self.table_id = dpg.add_table(header_row=False, policy=dpg.mvTable_SizingStretchProp)
        self.stage_id = dpg.add_stage()
        dpg.push_container_stack(self.stage_id)
        
    def add_widget(self, uuid, percentage, type=1):
        dpg.add_table_column(init_width_or_weight=percentage/100.0, parent=self.table_id)
        dpg.set_item_width(uuid, -1)

    def submit(self):
        dpg.pop_container_stack() # pop stage
        with dpg.table_row(parent=self.table_id):
            dpg.unstage(self.stage_id)  

class ClientManager:
    email = ''
    pw = ''
    recipient = ''
    selected_server = 'smtp.gmail.com'
    port = 465
    current_message=''''''

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


