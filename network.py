import smtplib, ssl
import dearpygui.dearpygui as dpg
import imaplib, email
import datetime
from data import *
from imap_tools import MailBox, A
from datetime import date



class SMTPHelper:
    def __init__(self, user, pw, smtp_server='smtp.gmail.com', port=465):
        self.smtp_server = smtp_server
        self.port = port    #SSL=465, TLS=587
        self.user = user
        self.pw = pw
        self.server = smtplib.SMTP_SSL(self.smtp_server, self.port)
        self.logged_in = False

    def login(self):
        try:
            self.server.login(self.user, self.pw)
            self.logged_in = True
            return 1
        except Exception as e:
            return str(e)

    def send_mail(self, recipient, subject, message: str):
        if not self.logged_in:
            self.login()

        message = "Subject: {}\n\n{}".format(subject, message)
        self.server.sendmail(self.user, recipient, message)


class IMAPHelper:
    def __init__(self, user, password, imap_server='imap.gmail.com'):
        self.imap_server = imap_server
        self.user = user
        self.pw = password
        self.mail = imaplib.IMAP4_SSL(self.imap_server)
        self.email_list = EmailList()

    def fetch_inbox(self):
        with MailBox(self.imap_server).login(self.user, self.pw, 'INBOX') as mailbox:
            cur_date = date.today()  
            for msg in mailbox.fetch(A(date_gte=datetime.date(cur_date.year, cur_date.month, cur_date.day-1))):
                email = Email(sender=msg.from_, subject=msg.subject, body=msg.text or msg.html, date=msg.date_str)
                self.email_list.add(email)
        return self.email_list
        