import requests
import random
import string
import time
import os



def delete_mail(mail=''):
    url = 'https://www.1secmail.com/mailbox'

    data = {
        'action': 'celeteMailbox',
        'login': mail.split("@")[0],
        'domain': mail.split("@")[1]
    }

    r = requests.post(url, data=data)
    print(f'[X] Почтовый адрес {mail} - удален!\n')