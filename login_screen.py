import dearpygui.dearpygui as dpg
from helpers import *
from network import *
from themes import *
from globals import *
import time




class LoginScreen():
    def __init__(self, fonts, app):
        self.f = fonts

        def selected_email_cb(s, d):
            client.selected_server = dpg.get_value(s)
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
        
        def login_cb(s, d):
            client.email = dpg.get_value(email_input)
            client.pw = dpg.get_value(pw_input)
            mail = SMTPHelper(email=client.email, password=client.pw, smtp_server=client.selected_server)

            login_status = mail.login()
            #login_status = 1
            if login_status == 1:
                dpg.set_value(login_text, 'Login Success')
                dpg.configure_item(login_text, color=(95, 255, 95))
                dpg.show_item(login_text)
                dpg.hide_item(login_error)
                dpg.show_item(self.login_status_group)
                #dpg.set_value('user_email_text', str(client.email))
                time.sleep(2)
                self.go_to_screen('send_screen')
            else:
                dpg.set_value(login_text, 'Login Failed:')
                dpg.configure_item(login_text, color=(255, 50, 50))
                dpg.set_value(login_error, str(login_status))     
                dpg.show_item(login_text)
                dpg.show_item(login_error)   
                dpg.show_item(self.login_status_group)
                time.sleep(2)
                self.go_to_screen('send_screen')



        with dpg.window(width=config['win_width'], height=config['win_height'], no_title_bar=True, no_resize=True, no_move=True, tag='self.login_screen') as self.login_screen:
            dpg.bind_font(fonts.title_font2)
        
            with dpg.group() as landing_group:
                title_text = dpg.add_text(f"Python {config['app_title']}")
                dpg.bind_item_font(title_text, self.f.title_font1)
                dpg.add_spacer()
                dpg.add_spacer()

                with dpg.group() as self.email_list_group:
                    dpg.add_text('Select the SMTP email server:')

                    email_list = dpg.add_listbox(label='', items=MAIL_LIST, width=300, callback=selected_email_cb, num_items=4)
                    
                    with dpg.group(horizontal=True, horizontal_spacing=4) as server_input_group:
                        server_input = dpg.add_input_text(default_value='', callback=server_input_cb, width=235, multiline=False, show=False, hint='Enter server')
                        port_input = dpg.add_input_text(default_value='', callback=port_input_cb, width=60, multiline=False, show=False, hint='Port')
                    
                    #set the styling of the server_input_group

                
                with dpg.group(pos=[100, 100]) as self.common_ports_group:
                    dpg.add_text('Common SMTP ports:')
                    t1 = dpg.add_text('TLS: 587')
                    dpg.add_text('SSL: 465')

            with dpg.child_window(width=300, height=190) as self.login_group:
                dpg.add_text('Email Address:')
                email_input = dpg.add_input_text(default_value='', width=272, multiline=False)
                dpg.add_text('Password:')
                pw_input = dpg.add_input_text(default_value='', width=272, multiline=False, password=True)
                dpg.add_button(label='Login', width=272, callback=login_cb)


            with dpg.child_window(width=-1, height=40, show=False) as self.login_status_group:
                with dpg.group(horizontal=True):
                    login_text = dpg.add_text(label='Login Successful', show=False)
                    login_error = dpg.add_text(label='Error', show=False)

    def show(self):
        dpg.show_item('self.login_screen')
    
    def hide(self):
        dpg.show_item('self.login_screen')
    
    def go_to_screen(screen):
        dpg.hide_item('self.login_screen')
        dpg.show_item(screen)
