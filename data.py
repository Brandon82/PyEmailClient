from dataclasses import dataclass

@dataclass
class Config:
    app_title: str
    win_width: int
    win_height: int

@dataclass
class Email:
    sender: str
    subject: str
    body: str
    date: str

class EmailList:
    def __init__(self):
        self.email_list = []

    def add(self, email: Email):
        self.email_list.append(email)

    def get_email(self, index):
        return self.email_list[index]

    def get_emails(self):
        return self.email_list

    def get_email_count(self):
        return len(self.email_list)

    def clear(self):
        self.email_list.clear()

    def __str__(self):
        return str(self.email_list)
    
    def __len__(self):
        return len(self.email_list)

@dataclass
class ClientManager:
    email: str = ''
    pw: str = ''
    recipient: str = ''
    selected_server: str = 'smtp.gmail.com'
    port: int = 465
    current_message: str = ''''''
    current_subject: str = ''
    email_list: EmailList = EmailList()