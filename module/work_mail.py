import mail_pars
import sort_direct
import sort_tech
import send_mess
import datetime

def mail():

    # Техники КТО

        # k495 = kto_tech_1 = Север
        # k582 = kto_tech_2 = Булдаков_С
        # k117 = kto_tech_3 = Кудрявцев_А
        # k633 = kto_tech_4 = Ува и район
        # k344 = kto_tech_5 = Федюнов_Н
        # k383 = kto_tech_6 = Шадрин_Г
        # k106 = kto_tech_7 = Плетнев_П
        # k980 = kto_tech_9 = Яшин Г

    # Техники ФУЛЛ

        # k495 = full_tech_1 = Абашев_А
        # k502 = full_tech_2 = Завьялов_Н
        # k117 = full_tech_3 = Кудрявцев_А
        # k633 = full_tech_4 = Ува и район
        # k472 = full_tech_5 = Малекин_А

    # Техники Н.Концепт

        # k495 = new_tech_1 = Север
        # k117 = new_tech_2 = Кудрявцев_А
        # k633 = new_tech_3 = Ува и район
        # k228 = new_tech_4 = Юданов_С

    # Каналы

    k495 = '-1002167206495' 'Север'
    k582 = '-1002174436582'
    k502 = '-1002135018502'
    k117 = '-1002170795117'
    k633 = '-1002149688633'
    k472 = '-1002148412472'
    k344 = '-1002200909344'
    k383 = '-1002228403383'
    k106 = '-1002203331106'
    k228 = '-1002163771228'
    k247 = '-1002248392247' 'Не используется'
    k980 = '-1002163832980' 'Не используется'
    k041 = '-1002233608041' 'Не используется'
    k214 = '-1002210202214'

    # test = '-1002202663906'

    mail_name = "help_alexstroy@mail.ru"
    mail_pass = "09X7BYAayMx9vH7Lqu2t"

    while True:

        letter = mail_pars.mail(mail_name, mail_pass)

        if letter != None:
            title = (letter.split('\n')[0]).split()
            line = letter.split('\n')

            # Сортирует задачи
            if title[0] == 'Зарегистрирована' and title[1] == 'новая' and title[2] == 'задача':

                # Создает переменные строк
                numb_shop = ((line[3].split()[2]).replace(',', ''))
                task_inc = line[5]

                # Создает формат сообщения задачи
                task = [line[0], line[1], line[2], line[3], line[5], line[6]]

                # Фильтрует задачу по классу инцидента КТО
                if sort_direct.sort(task_inc, 'kto') == True:

                    # Фильтрует задачу по технику КТО
                    sort_tech.tech(task, numb_shop, 8, 'kto', k495, k582, k117, k633, k344, k383, k106, k495, k980, 0)

                # Фильтрует задачу по классу инцидента ФУЛЛ
                elif sort_direct.sort(task_inc, 'full') == True:

                    # Фильтрует задачу по технику ФУЛЛ
                    sort_tech.tech(task, numb_shop, 6, 'full', k495, k502, k117, k633, k472, k495, 0, 0, 0, 0)

                # Фильтрует задачу по классу инцидента New_conc
                elif sort_direct.sort(task_inc, 'new') == True:

                    # Фильтрует задачу по технику
                    sort_tech.tech(task, numb_shop, 5, 'new', k495, k117, k633, k228, k495, 0, 0, 0, 0, 0)

                else:
                    send_mess.take_mess(task, '-1002243705128')


            # Сортирует ициденты
            elif title[0] == 'Зарегистрирован' and title[1] == 'инцидент,':  # Фильтр ицидентов

                param = line[7].split(',')
                parametrs = ((param[0]).split(':')[2]).strip()
                print(parametrs)

                if parametrs != 'Обязательный параметр':
                    # Создает переменные строк
                    numb_shop = (((((line[4]).split())[1]).replace('_', ' ')).split())[1]

                    # Создает формат сообщения инцидента
                    inced = [line[0], line[1], line[2], line[4], line[5], line[6], line[7], line[8], line[9], line[10]]

                    # Фильтрует задачу по технику ФУЛЛ
                    sort_tech.tech(inced, numb_shop, 6, 'full', k495, k502, k117, k633, k472, k495, 0, 0, 0, 0)

                elif parametrs == 'Обязательный параметр':
                    # Создает формат сообщения инцидента
                    inced = [line[0], line[1], line[2], line[4], line[5], line[6], line[7], line[8], line[9], line[10]]
                    send_mess.take_mess(inced, k214)

                elif parametrs == 'Параметр ХО не соответствует ТЗ':
                    # Создает формат сообщения инцидента
                    inced = [line[0], line[1], line[2], line[4], line[5], line[6], line[7], line[8], line[9], line[10]]
                    send_mess.take_mess(inced, k214)



        else:
            current_time = datetime.datetime.now().time()
            print('Заявок нет')
            print(current_time)
            print('\n')
            break