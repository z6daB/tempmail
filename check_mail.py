import requests
import random
import string
import time
import os

API = 'https://www.1secmail.com/api/v1/'


def check_mail(mail=''):
    req_link = f'{API}?action=getMessages&login={mail.split("@")[0]}&domain={mail.split("@")[1]}'
    r = requests.get(req_link).json()
    lenght = len(r)

    if lenght == 0:
        print('[INFO] На почте пока писем нет. Проверка происходит автоматически каждые 5 сек.')
    else:
        id_list = []
        for i in r:
            for k, v in i.items():
                if k == 'id':
                    id_list.append(v)
            print(f'[+] У вас {lenght} входящих! Почта обнавляется автоматически каждые 5 секунд!')

            current_dic = os.getcwd()
            final_dir = os.path.join(current_dic, 'all_mails')

            if not os.path.exists(final_dir):
                os.makedirs(final_dir)

            for i in id_list:
                reed_msg = f'{API}?action=readMessage&login={mail.split("@")[0]}&domain={mail.split("@")[1]}&id={i}'
                r = requests.get(reed_msg).json()

                sender = r.get('from')
                subject = r.get('subject')
                date = r.get('date')
                content = r.get('textBody')

                mail_file_path = os.path.join(final_dir, f'{i}.txt')

                with open(mail_file_path, 'w') as file:
                    file.write(f'Sender: {sender}\nTo: {mail}\nSubject: {subject}\nDate: {date}\nContent: {content}')
