import requests
import random
import string
import time
import os
from delete_mail import delete_mail
from generate_mail import generate_username
from check_mail import check_mail

API = 'https://www.1secmail.com/api/v1/'
domain_list = ["1secmail.com",
               "1secmail.org",
               "1secmail.net"]

domain = random.choice(domain_list)


def main():
    try:
        username = generate_username()
        mail = f'{username}@{domain}'
        print(f'[+] Ваш почтовый адрес: {mail}')

        mail_req = requests.get(f'{API}?login={mail.split("@")[0]}&domain={mail.split("@")[1]}')

        while True:
            check_mail(mail=mail)
            time.sleep(5)

    except(KeyboardInterrupt):
        delete_mail(mail=mail)
        print('Программа прервана!')


if __name__ == '__main__':
    main()
