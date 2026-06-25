import mail_pars
import sort_direct
import sort_tech
import send_max_mess
from datetime import date
import time
from config import format_date, mail_name, mail_pass, params, no_class
from config import group_1, group_2, group_3, group_4, group_5, group_6
from config import group_7, group_8, group_9, group_10, group_11, group_12
from config import group_13

def mail():
    try:
        while True:

            letter = mail_pars.mail(mail_name, mail_pass)

            if letter is not None:
                title = (letter.split('\n')[0]).split()
                line = letter.split('\n')

                estimate_canceled = ((line[0]).split(' '))[0] + ((line[0]).split(' '))[1] # Смета отменена
                estimate_returned = ((line[0]).split(' '))[0] + ((line[0]).split(' '))[1] + ((line[0]).split(' '))[2] # Смета на доработку
                # estimate_agreed = ((line[0]).split(' '))[0] + ((line[0]).split(' '))[5] # Смета согласована
                estimate_reserved = ((line[0]).split(' '))[0] + ((line[0]).split(' '))[1] + ((line[0]).split(' '))[4] + ((line[0]).split(' '))[5]  # Резерв получен

                # Сортирует задачи
                if title[0] == 'Зарегистрирована' and title[1] == 'новая' and title[2] == 'задача':

                    # Создает переменные строк
                    numb_shop = ((line[3].split()[2]).replace(',', ''))
                    task_inc = line[5]

                    # Изменение конечной даты (Сторонний код)
                    first_date = line[1][21] + line[1][22] + line[1][23] + line[1][24] + line[1][18] + line[1][19] + \
                                 line[1][15] + line[1][16]
                    second_date = line[2][32] + line[2][33] + line[2][34] + line[2][35] + line[2][29] + line[2][30] + \
                                  line[2][26] + line[2][27]

                    start_date = date.fromisoformat(first_date)
                    end_date = date.fromisoformat(second_date)
                    delta = abs(start_date - end_date)

                    delta_date = delta.days

                    real_date = date.fromisoformat(first_date)

                    if delta_date <= 1:
                        new_data = real_date + delta
                    else:
                        new_data = real_date + delta / 2

                    new_date = ('Плановый срок устранения: ' + str(new_data)[8] + str(new_data)[9] + '.'
                                + str(new_data)[5] + str(new_data)[6] + '.'
                                + str(new_data)[0] + str(new_data)[1] + str(new_data)[2] + str(new_data)[3]
                                + line[2][36] + line[2][37] + line[2][38] + line[2][39] + line[2][40] + line[2][41]
                                + line[2][42] + line[2][43] + line[2][44] + line[2][45] + line[2][46]
                                + line[2][47] + line[2][48] + line[2][49] + line[2][50] + line[2][51] + line[2][52] +
                                line[2][53] + line[2][54])

                    # Создает формат сообщения задачи
                    task = [line[0], line[1], new_date, line[3], line[5], line[6]]
                    # Конец стороннего кода

                    # Создает формат сообщения задачи
                    # task = [line[0], line[1], line[2], line[3], line[5], line[6]]

                    # Фильтрует задачу по классу инцидента КТО
                    if sort_direct.sort(task_inc, 'kto'):

                        # Фильтрует задачу по технику КТО
                        sort_tech.tech(task, numb_shop, 6, 'kto', group_1, group_4, group_6, group_7, group_8, group_12, 0, 0, 0, 0)

                    # Фильтрует задачу по классу инцидента ФУЛЛ
                    elif sort_direct.sort(task_inc, 'full'):

                        # Фильтрует задачу по технику ФУЛЛ
                        sort_tech.tech(task, numb_shop, 5, 'full', group_2, group_4, group_5, group_9, group_11, 0, 0, 0, 0, 0)

                    # Фильтрует задачу по классу инцидента New_conc
                    elif sort_direct.sort(task_inc, 'new'):

                        # Фильтрует задачу по технику
                        sort_tech.tech(task, numb_shop, 3, 'new', group_3, group_4, group_10, group_11, 0, 0, 0, 0, 0, 0)

                    else:
                        send_max_mess.send_mess(task, no_class)

                # Сортирует инциденты
                elif title[0] == 'Зарегистрирован' and title[1] == 'инцидент,':

                    param = line[7].split(',')
                    parameters = ((param[0]).split(':')[2]).strip()

                    if parameters != 'Обязательный параметр':
                        # Создает переменные строк
                        numb_shop = (((((line[4]).split())[1]).replace('_', ' ')).split())[1]

                        # Создает формат сообщения инцидента
                        inced = [line[0], line[1], line[2], line[4], line[5], line[6], line[7], line[8], line[9], line[10]]

                        # Фильтрует задачу по технику ФУЛЛ
                        sort_tech.tech(inced, numb_shop, 4, 'full', group_2, group_4, group_5, group_9, 0, 0, 0, 0, 0, 0)

                    elif parameters == 'Обязательный параметр':
                        # Создает формат сообщения инцидента
                        inced = [line[0], line[1], line[2], line[4], line[5], line[6], line[7], line[8], line[9], line[10]]
                        send_max_mess.send_mess(inced, params)

                    elif parameters == 'Параметр ХО не соответствует ТЗ':
                        # Создает формат сообщения инцидента
                        inced = [line[0], line[1], line[2], line[4], line[5], line[6], line[7], line[8], line[9], line[10]]
                        send_max_mess.send_mess(inced, params)

                #Сортирует сметы
                elif estimate_canceled == 'Отмененасмета':
                    task = title
                    send_max_mess.send_mess(task,group_13)

                elif estimate_returned == 'Возвращенанадоработку':
                    task = title
                    send_max_mess.send_mess(task, group_13)

                # elif estimate_agreed == 'Сметасогласована.Необходимо':
                #     task = title
                #     send_max_mess.send_mess(task, group_13)

                elif estimate_reserved == 'ПоСметесозданзаказ.Номер':
                    task = title
                    send_max_mess.send_mess(task, group_13)

                else:
                    data = time.strftime(format_date)
                    print(data,' Новых заявок нет' )
                    print('\n')
                    break
            else:
                data = time.strftime(format_date)
                print(data, ' Новых писем нет')
                break
    except:
        print(time.strftime(format_date))
        print('Ошибка модуля обработки почты', '\n')