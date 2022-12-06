import dearpygui.dearpygui as dpg
import os
from helpers import *

config = {
    'app_title': 'Email Client',
    'win_width': 750,
    'win_height': 560,
}

client = ClientManager()

MAIL_LIST = ['smtp.gmail.com', 'smtp.mail.yahoo.com', 'other']

CUR_FILE_PATH = os.path.dirname(os.path.realpath(__file__))