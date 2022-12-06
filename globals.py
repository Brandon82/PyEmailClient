import dearpygui.dearpygui as dpg
from helpers import *

config = {
    'app_title': 'Email Client',
    'win_width': 750,
    'win_height': 560,
}

client = ClientManager()

MAIL_LIST = ['smtp.gmail.com', 'smtp.mail.yahoo.com', 'other']
