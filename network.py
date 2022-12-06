import smtplib, ssl
import dearpygui.dearpygui as dpg
import imaplib, email
from imap_tools import MailBox, AND

class SMTPHelper:
    def __init__(self, email, password, smtp_server='smtp.gmail.com', port=465):
        self.smtp_server = smtp_server
        self.port = port    #SSL=465, TLS=587
        self.email = email
        self.password = password
        self.server = None
        self.set_server()

    def set_server(self):
        context = ssl.create_default_context()
        self.server = smtplib.SMTP_SSL(self.smtp_server, self.port, context=context)
    
    def login(self):
        try:
            self.server.login(self.email, self.password)
            return 1
        except Exception as e:
            return str(e)
        
    def send_mail(self, recipient, message: str):
        context = ssl.create_default_context()
        self.server.login(self.email, self.password)
        self.server.sendmail(self.email, recipient, message)


class IMAPHelper:
    def __init__(self, email, password, imap_server='imap.gmail.com'):
        self.imap_server = imap_server
        self.email = email
        self.password = password
        self.connection = None
        self.is_logged_in = False
        self.set_connection()

    def set_connection(self):
        self.connection = imaplib.IMAP4_SSL(self.imap_server)
        self.connection.login(self.email, self.password)

    def fetch_inbox(self):
        x = self.connection.select('inbox', readonly=True)
        num = x[1][0].decode('utf-8')
        
        resp, lst = self.connection.fetch(num, '(RFC822)')
        body = lst[0][1]
        email_message = email.message_from_bytes(body)
        #print(email_message)
        print('From:' + email_message['From'])
        print('To:' + email_message['To'])
        print('Date:' + email_message['Date'])
        print('Subject:' + str(email_message['Subject']))
        print('Content:' + str(email_message.get_payload()[0]))
        print('------------------')