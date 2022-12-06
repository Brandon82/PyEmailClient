import dearpygui.dearpygui as dpg

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
        tag = dpg.get_item_configuration(s)
        print(str(tag))
        index = int(tag[-1])
        
        d.selected = index
        print(d.selected)
