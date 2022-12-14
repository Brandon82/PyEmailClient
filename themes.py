import dearpygui.dearpygui as dpg
from helpers import *


main_background_color = (40, 40, 40)
child_background_color = (30, 30, 30)
frame_bg_color = (50, 50, 50)
text_color = (255, 255, 255, 255)
accent_color = (104, 104, 204)
dark_accent_color = (104, 104, 204, 150)

def apply_tab_button_active(item, color):
    with dpg.theme() as tab_button_theme:
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, color)
    dpg.bind_item_theme(item, tab_button_theme)

def apply_tab_button_inactive(item):
    with dpg.theme() as tab_button_theme:
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (0, 0, 0, 0))  
    dpg.bind_item_theme(item, tab_button_theme)

def apply_main_theme():
    with dpg.theme() as mtheme:
        with dpg.theme_component(dpg.mvAll):
            # --- Styling ---
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4)
            dpg.add_theme_style(dpg.mvStyleVar_ChildRounding, 4)

            dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 6, 6)  
            dpg.add_theme_style(dpg.mvStyleVar_ItemInnerSpacing, 4, 6)  

            dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 14, 10)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 4, 3)
        
            # --- Colors ---
            dpg.add_theme_color(dpg.mvThemeCol_Text, text_color)
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, main_background_color)
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg, child_background_color)

            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, frame_bg_color)

            dpg.add_theme_color(dpg.mvThemeCol_Button, accent_color)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, accent_color)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, accent_color)

            dpg.add_theme_color(dpg.mvThemeCol_CheckMark, accent_color)
            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarBg, accent_color)
            
            dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, accent_color)
            dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, accent_color)
            dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, accent_color)

            # Best way to completely disable borders:
            # other methods may interfere with padding
            dpg.add_theme_color(dpg.mvThemeCol_Border, (0, 0, 0, 0))

        with dpg.theme_component(dpg.mvChildWindow):
            # --- Child Styling ---
            # --- Child Color ---
            dpg.add_theme_color(dpg.mvThemeCol_Text, text_color)

        dpg.bind_theme(mtheme)
    