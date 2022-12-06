import dearpygui.dearpygui as dpg

class TabBarManager:
    def __init__(self, num, list, item_list):
        self.num = num
        self.list = list
        self.item_list = item_list
        self.selected = 0

        def tab_cb(s, d, u):
            index = int(u[-1])
            self.selected = index
            update_state()
        
        def update_state():
            for i in range(self.num):
                if i == self.selected:
                    dpg.show_item(self.item_list[i])
                else:
                    dpg.hide_item(self.item_list[i])

        with dpg.group(horizontal=True) as self.tab_bar:
            #for each element in the list
            for i in range(self.num):
                print(i)
                dpg.add_button(label=self.list[i], width=100, callback=tab_cb, tag=f'tab-{i}', user_data=f'tab-{i}')
        
    

