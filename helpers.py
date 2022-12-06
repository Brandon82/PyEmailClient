import dearpygui.dearpygui as dpg
from sys import platform
import os

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
    CUR_FILE_PATH = os.path.dirname(os.path.realpath(__file__))
    email = ''
    pw = ''
    recipient = ''
    selected_server = 'smtp.gmail.com'
    port = 465
    current_message=''''''
    platform = platform

class FontManager:
    def __init__(self, c):
        with dpg.font_registry():
            if platform == 'darwin':
                self.h1_b = dpg.add_font((c.CUR_FILE_PATH) + '/Fonts/OpenSans-Bold.ttf', 34)
                self.h2_b = dpg.add_font((c.CUR_FILE_PATH) + '/Fonts/OpenSans-Bold.ttf', 22)

                self.b2 = dpg.add_font((c.CUR_FILE_PATH) + '\Fonts\OpenSans-Regular.ttf', 22)
                self.b2_sb = dpg.add_font((c.CUR_FILE_PATH) + '\Fonts\OpenSans-Regular.ttf', 22)

            elif platform == 'win32':
                self.h1_b = dpg.add_font((c.CUR_FILE_PATH) + '\Fonts\OpenSans-Bold.ttf', 34)
                self.h2_b = dpg.add_font((c.CUR_FILE_PATH) + '\Fonts\OpenSans-Bold.ttf', 22)

                self.b2 = dpg.add_font((c.CUR_FILE_PATH) + '\Fonts\OpenSans-Regular.ttf', 22)
                self.b2_sb = dpg.add_font((c.CUR_FILE_PATH) + '\Fonts\OpenSans-SemiBold.ttf', 22)

class TabBarManager:
    def __init__(self, num, list):
        self.num = num
        self.list = list
        self.selected = 0
        
        with dpg.group(horizontal=True) as self.tab_bar:
            #for each element in the list
            for i in range(self.num):
                print(i)
                dpg.add_button(label=self.list[i], width=100, callback=self.tab_cb, tag=f'tab-{i}', user_data=self)
    
    def tab_cb(s, d):
        tag = dpg.get(s)
        print(tag)
        index = int(tag[-1])
        
        d.selected = index
        print(d.selected)

        if d.selected == index:



    def tabbar_cb(s, d):
        print(s)
        if s == 45:
            dpg.hide_item(remail_group)
            dpg.show_item(email_group)
        elif s == 46:
            dpg.hide_item(email_group)
            dpg.show_item(remail_group)



