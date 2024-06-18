from email.header import decode_header
from bs4 import BeautifulSoup
import re
import time
import requests

import mail_pars
import sort_direct

# Техники
# Gorev_A = '-1002203331106' #KTO (kto_tech_1)
# Buldakob_S = '-1002174436582' #KTO (kto_tech_2)
# Kuznecov_A = '-1002149688633' #KTO (kto_tech_3)
# Malich_O = '-1002228403383' #KTO (kto_tech_4)
# Abashev_A = '-1002167206495' #KTO (kto_tech_5)
# Belich_A = '-1002248392247' #KTO (kto_tech_6)
# Technic_K = '-1002210202214' #KTO (kto_tech_7)
#
# Zavyalov_N = '-1002135018502' #FULL (full_tech_1)
# Malekin_A = '-1002148412472' #FULL (full_tech_2)
# Kudravcev_A = '-1002170795117' #FULL (full_tech_3)
# Technic_F = '-1002163832980' #FULL (full_tech_4)

Test = '-1002202663906'

# mail_name = "test-alexstroy@mail.ru" # Тест почта
# mail_pass = "BGBLZdH6gbCQyTtY9PYv" # Тест пароль

mail_name = "help_alexstroy@mail.ru"
mail_pass = "09X7BYAayMx9vH7Lqu2t"

def take_mess(mess, id):
    time.sleep(5)
    TOKEN = "7240204692:AAHiUSc0DdlcN2YEZsj-xbLgc9EqCpkMV1Q"
    chat_id = id
    message = str(' '.join(mess))
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json())  # Эта строка отсылает сообщение

# Период запроса на сервер
request_period = 5

# Запускает запрос новых писем и их обработку
while True:

    num_letters = mail_pars.mail(mail_name, mail_pass)
    letter = mail_pars.mail(mail_name, mail_pass)

    if num_letters != 0 and letter != None:

        lines = letter[0].split('\n')
        new_task = lines[0]
        row_task = new_task.split(' ')
        new_num = lines[3]
        new_shop = new_num.split(' ')

        # Сортирует задачи
        if row_task[0] == 'Зарегистрирована' and row_task[1] == 'новая' and row_task[2] == 'задача':

            # Создает формат сообщения задачи
            task = [lines[0], lines[1], lines[2], lines[3], lines[5], lines[6]]

            # Фильтрует задачу по классу инцидента КТО
            if sort_shop.sort(task, 'kto') == True:

                # Фильтрует задачу по технику КТО
                for i in range(7):
                    num_k = i + 1
                    num_tech = '../documents/kto_tech_' + str(num_k) + '.txt'
                    kto_tech = open(num_tech, 'r', encoding='utf-8')
                    kTech = kto_tech.read().splitlines()
                    kto_tech.close()
                    for i in kTech:
                        num_call = num_k
                        abonent_kto = i.strip()
                        new_kto = new_shop[2].strip().replace(',', "")
                        if new_kto == abonent_kto and num_call == 1:
                            take_mess(task, Test)
                        elif new_kto == abonent_kto and num_call == 2:
                            take_mess(task, Test)
                        elif new_kto == abonent_kto and num_call == 3:
                            take_mess(task, Test)
                        elif new_kto == abonent_kto and num_call == 4:
                            take_mess(task, Test)
                        elif new_kto == abonent_kto and num_call == 5:
                            take_mess(task, Test)
                        elif new_kto == abonent_kto and num_call == 6:
                            take_mess(task, Test)
                        elif new_kto == abonent_kto and num_call == 7:
                            take_mess(task, Test)
                        else:
                            continue

            # Фильтрует задачу по классу инцидента ФУЛЛ
            if sort_shop.sort(task, 'full') == True:

                # Фильтрует задачу по технику ФУЛЛ
                for i in range(4):
                    num_f = i + 1
                    num_tech = '../documents/full_tech_' + str(num_f) + '.txt'
                    full_tech = open(num_tech, 'r', encoding='utf-8')
                    fTech = full_tech.read().splitlines()
                    full_tech.close()
                    for i in fTech:
                        num_call = num_f
                        abonent_full = i.strip()
                        new_full = new_shop[2].strip().replace(',', "")
                        if new_full == abonent_full and num_call == 1:
                            take_mess(task, Test)
                        elif new_full == abonent_full and num_call == 2:
                            take_mess(task, Test)
                        elif new_full == abonent_full and num_call == 3:
                            take_mess(task, Test)
                        elif new_full == abonent_full and num_call == 4:
                            take_mess(task, Test)
                        else:
                            continue

        # Сортирует ициденты
        elif row_task[0] == 'Зарегистрирован' and row_task[1] == 'инцидент,': # Фильтр ицидентов
            inced = [lines[0], lines[1], lines[2], lines[4], lines[5], lines[6], lines[7], lines[8], lines[9], lines[10]]

            # Обрабатывает строку с адресом
            strok_inc = inced[3].strip().replace('_', ' ')
            new_inc = strok_inc.split(' ')

            # Фильтрует задачу по технику ФУЛЛ
            for i in range(4):
                num = i + 1
                num_tech = '../documents/full_tech_' + str(num) + '.txt'
                full_tech = open(num_tech, 'r', encoding='utf-8')
                fTech = full_tech.read().splitlines()
                full_tech.close()
                for i in fTech:
                    num_call = num
                    abonent_full = i.strip()
                    new_full = new_inc[2].strip().replace(',', "")
                    if new_full == abonent_full and num_call == 1:
                        take_mess(inced, Test)
                    elif new_full == abonent_full and num_call == 2:
                        take_mess(inced, Test)
                    elif new_full == abonent_full and num_call == 3:
                        take_mess(inced, Test)
                    elif new_full == abonent_full and num_call == 4:
                        take_mess(inced, Test)
                    else:
                        continue
        else:
            continue

    else:
        print('нет сообщений')







# Выход с почтового сервера
imap.close()
imap.logout()

# Таймер периода запроса
time.sleep(request_period)


