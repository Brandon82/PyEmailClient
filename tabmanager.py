import dearpygui.dearpygui as dpg
from themes import *

class TabBarManager:
    def __init__(self, num, list, item_list):
        self.num = num
        self.list = list
        self.item_list = item_list
        self.selected = 0

        def tab_cb(s, d, u):
            self.selected = u
            update_state()
        
        def update_state():
            for i in range(self.num):
                if i == self.selected:
                    dpg.show_item(self.item_list[i])
                    apply_tab_button_active(item=f'tab-{i}', color=accent_color)
                else:
                    dpg.hide_item(self.item_list[i])
                    apply_tab_button_inactive(item=f'tab-{i}')

        with dpg.group(horizontal=True) as self.tab_bar:
            for i in range(self.num):
                print(i)
                dpg.add_button(label=self.list[i], width=100, callback=tab_cb, tag=f'tab-{i}', user_data=i)
            update_state()