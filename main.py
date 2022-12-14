import dearpygui.dearpygui as dpg
import os
import smtplib, ssl
import time
from dearpygui.demo import show_demo
from threading import Timer
from themes import *
from helpers import *
from network import *
from globals import *
from tabmanager import *
from fontmanager import *
from data import *
from enum import Enum, auto


def main():
    def auto_center_cb(s, d):
        win_width = dpg.get_item_width(login_screen)
        win_height = dpg.get_item_height(login_screen)

        if (win_width < 634 and dpg.does_item_exist(login_screen)):
            dpg.hide_item(common_ports_group)
        else:
            dpg.show_item(common_ports_group)

        list_width = dpg.get_item_rect_size(item=email_list_group)[0]
        dpg.set_item_pos(item=email_list_group, pos=[(win_width/2)-(list_width/2), 80])

        login_width = dpg.get_item_rect_size(item=login_group)[0]
        dpg.set_item_pos(item=login_group, pos=[(win_width/2)-(login_width/2), 280])
        
        helper_pos = dpg.get_item_pos(item=email_list_group)
        dpg.set_item_pos(item=common_ports_group, pos=[10, helper_pos[1]])

        dpg.set_item_pos(item=login_status_group, pos=[16, win_height-80])


        dpg.set_item_pos(item=tab.tab_bar, pos=[dpg.get_item_width(email_screen)-220, 92])


    def leave_login_screen():
        dpg.hide_item(login_screen)
        dpg.show_item(email_screen)
        dpg.set_primary_window(email_screen, True)

    def login_cb(s, d):
        client.email = dpg.get_value('email_input')
        client.pw = dpg.get_value('pw_input')

        mail = SMTPHelper(user=client.email, pw=client.pw, smtp_server=client.selected_server)

        login_status = mail.login()
        #login_status = 1
        if login_status == 1:
            dpg.set_value(login_text, 'Login Successful')
            dpg.configure_item(login_text, color=(95, 255, 95))
            dpg.show_item(login_text)
            dpg.hide_item(login_error)
            dpg.show_item(login_status_group)
            dpg.set_value(user_email_text, str(client.email))
            time.sleep(2)
            leave_login_screen()
        else:
            dpg.set_value(login_text, 'Login Failed:')
            dpg.configure_item(login_text, color=(255, 50, 50))
            dpg.set_value(login_error, str(login_status))     
            dpg.show_item(login_text)
            dpg.show_item(login_error)   
            dpg.show_item(login_status_group)
            time.sleep(2)
            leave_login_screen()

    def selected_email_cb(s, d):
        client.selected_server = dpg.get_item_user_data(s)
        if client.selected_server == MAIL_LIST[-1]:
            dpg.show_item(server_input)
            dpg.show_item(port_input)
        else:
            dpg.hide_item(server_input)
            dpg.hide_item(port_input)

    def server_input_cb(s, d):
        client.selected_server = dpg.get_value(s)

    def email_note_cb(s, d):
        client.current_message = dpg.get_value(s)
    
    def port_input_cb(s, d):
        client.port = dpg.get_value(s)
    
    def subj_inp_cb(s, d):
        client.current_subject = dpg.get_value(s)
    


    def send_message_cb(s, d):
        if client.current_message != '''''':
            mail = SMTPHelper(user=client.email, pw=client.pw, smtp_server=client.selected_server)
            mail.send_mail(client.recipient, client.current_subject, client.current_message)
            dpg.set_value(note_input, '')
            client.current_message = ''
            dpg.set_value(note_input, client.current_message)
            client.current_subject = ''
            dpg.set_value(note_input, client.current_subject)

    def delete_message_cb(s, d):
        client.current_message = ''
        dpg.set_value(note_input, client.current_message)

    def recip_email_cb(s, d):
        client.recipient = dpg.get_value(s)
    
    def parse_inbox_cb(s, d):
        imap = IMAPHelper(client.email, client.pw)
        client.email_list = imap.fetch_inbox()

        dpg.show_item(emaillistwrapper_group)

        for i in range(len(client.email_list)):
            email = client.email_list.get_email(i)
            dpg.set_value(f'e{i+1}_from_t', str(email.sender))
            dpg.set_value(f'e{i+1}_date_t', str(email.date))
            dpg.set_value(f'e{i+1}_subj_t', str(email.subject))
            #dpg.set_value(f'e{i+1}_body_t', email.body)
            





    dpg.create_context()

    f = FontManager(get_file_path())

    with dpg.window(width=config['win_width'], height=config['win_height'], no_title_bar=True, no_resize=True, no_move=True) as login_screen:
        dpg.bind_font(f.b2_sb)

        with dpg.group() as landing_group:
            title_text = dpg.add_text(f"Python {config['app_title']}")
            dpg.bind_item_font(title_text, f.h1_b)
            dpg.add_spacer()
            dpg.add_spacer()

            with dpg.group() as email_list_group:
                dpg.add_text('Select the SMTP email server:')

                email_list = dpg.add_listbox(label='', items=MAIL_LIST, width=300, callback=selected_email_cb, num_items=4)
                
                with dpg.group(horizontal=True, horizontal_spacing=4) as server_input_group:
                    server_input = dpg.add_input_text(default_value='', callback=server_input_cb, width=235, multiline=False, show=False, hint='Enter server')
                    port_input = dpg.add_input_text(default_value='', callback=port_input_cb, width=60, multiline=False, show=False, hint='Port')
                
            
            with dpg.group(pos=[100, 100]) as common_ports_group:
                dpg.add_text('Common SMTP ports:')
                t1 = dpg.add_text('TLS: 587')
                dpg.add_text('SSL: 465')

        with dpg.child_window(width=300, height=210) as login_group:
            
            dpg.add_spacer(height=4)
            dpg.add_text('Email Address:', indent=20)

            line1 = LayoutHelper()
            line1. add_widget(dpg.add_spacer(), .05)
            line1.add_widget(dpg.add_input_text(default_value='grabowski2001@gmail.com', tag='email_input', width=232, multiline=False), .90)
            line1.add_widget(dpg.add_spacer(), .05)
            line1.submit()


            dpg.add_text('Password:', indent=20)
            line2 = LayoutHelper()
            line2. add_widget(dpg.add_spacer(), .05)
            line2.add_widget(dpg.add_input_text(default_value='ikrkdqojefbxjwja', tag='pw_input', width=232, multiline=False, password=True), .90)
            line2.add_widget(dpg.add_spacer(), .05)
            line2.submit()

            dpg.add_button(label='Login', width=232, pos=[(dpg.get_item_width(login_group)-232)/2, dpg.get_item_height(login_group)-48], callback=login_cb)

        with dpg.group(horizontal=True, show=False) as login_status_group:
            login_text = dpg.add_text(label='Login Successful', show=False)
            login_error = dpg.add_text(label='Error', show=False)
        

    with dpg.window(width=config['win_width'], height=config['win_height'], no_resize=True, no_move=True, no_title_bar=True, show=False) as email_screen:
        dpg.bind_font(f.b2_sb)

        with dpg.group() as email_group:   
            dpg.add_spacer(height=2)
            user_email_text = dpg.add_text('My Email: ')
            dpg.add_spacer(height=2)

            recip_email_input = dpg.add_input_text(default_value='', multiline=False, hint='Enter recipitent Email', callback = recip_email_cb, width=300)

            email_title_text = dpg.add_text('Enter your message:')
            subj_inp = dpg.add_input_text(default_value='', width=-1, hint='Subject', callback=subj_inp_cb)
            note_input = dpg.add_input_text(default_value='', callback=email_note_cb, multiline=True, height=-100, width=-1)

            with dpg.group(horizontal=True) as send_email_group:
                dpg.add_button(label='Send Email', width = 160, height = 30, callback = send_message_cb)
                dpg.add_button(label='Delete Email', width = 160, height = 30, callback = delete_message_cb)

        with dpg.group(show=False) as inbox_group:
            dpg.add_text('Emails:')


            dpg.add_spacer(height=42)
            dpg.add_radio_button(items=['IMAP', 'POP'], default_value=0, horizontal=True)

            with dpg.child_window(height = -100, width=-1, no_scrollbar=True) as email_1:
                with dpg.group(show=False) as emaillistwrapper_group:
                    for i in range(10):
                        dpg.add_text('', tag=f'e{i+1}_from_t')
                        dpg.add_text('', tag=f'e{i+1}_subj_t')
                        dpg.add_text('', tag=f'e{i+1}_date_t')
                        with dpg.drawlist(width=500, height=6):
                            dpg.draw_line((0, 0), (500, 0), color=child_background_color, thickness=4)

            dpg.add_button(label='Fetch Inbox', width = 160, height = 30, callback=parse_inbox_cb)

        tab = TabBarManager(num=2, list=['Send Mail', 'Inbox'], item_list=[email_group, inbox_group])


    with dpg.theme() as email_list_group_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, dark_accent_color)
            dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, dark_accent_color)
            dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, dark_accent_color)

        with dpg.theme_component(dpg.mvListbox):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, child_background_color, category=dpg.mvThemeCat_Core)

        with dpg.theme_component(dpg.mvInputText):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, child_background_color, category=dpg.mvThemeCat_Core)

        with dpg.theme_component(dpg.mvInputInt):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, child_background_color, category=dpg.mvThemeCat_Core)

    with dpg.theme() as login_group_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 0, 0)  

    with dpg.theme() as send_page_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, child_background_color, category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg, frame_bg_color, category=dpg.mvThemeCat_Core)


    #show_demo()
    #dpg.show_style_editor()

    apply_main_theme()
    dpg.bind_item_theme(email_list_group, email_list_group_theme)
    dpg.bind_item_theme(login_group, login_group_theme)
    dpg.bind_item_theme(email_screen, send_page_theme)

    dpg.create_viewport(title=config['app_title'], width=config['win_width'] + 16, height=config['win_height'] + 38, min_height=600, min_width=340)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window(login_screen, True)

    dpg.set_viewport_resize_callback(auto_center_cb)
    auto_center_cb(None, None)

    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    main()