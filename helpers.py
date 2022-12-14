import dearpygui.dearpygui as dpg
from sys import platform
import os
from dataclasses import dataclass
from data import *


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
