import mail_pars
import sort_direct
import sort_tech
import send_mess
import datetime
from datetime import date

def mail():

    # Каналы

    k214 = '-1002210202214' # Нарушение параметра
    k582 = '-1002174436582' # Булдаков С - kto_tech_1
    k502 = '-1002135018502' # Завьлов Н - full_tech_1
    k117 = '-1002170795117' # Кудрявцев А - kto_tech_2, full_tech_2, new_tech_2
    k633 = '-1002149688633' # Ува и район - full_tech_4, new_tech_3
    k472 = '-1002148412472' # Малекин А - full_tech_3
    k344 = '-1002200909344' # Федюнов Н - kto_tech_4, new_tech_4
    k383 = '-1002228403383' # Шадрин Г - kto_tech_5
    k106 = '-1002203331106' # Плетнев П - kto_tech_3
    k228 = '-1002163771228' # Юданов С - new_tech_1
    k980 = '-1002163832980' # Яшин Г - kto_tech_6
    k128 = '-1002243705128' # Нет класса инцидента
    k247 = '-1002248392247' #Не используется
    k041 = '-1002233608041' #Не используется
    k495 = '-1002167206495' #Не испоьзуется
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



                # Изменение конечной даты
                a = line[1]
                b = line[2]

                first_date = a[21] + a[22] + a[23] + a[24] + a[18] + a[19] + a[15] + a[16]
                second_date = b[32] + b[33] + b[34] + b[35] + b[29] + b[30] + b[26] + b[27]

                aa = date.fromisoformat(first_date)
                bb = date.fromisoformat(second_date)
                delta = abs(aa - bb)

                real_date = date.fromisoformat(first_date)
                new_data = real_date + delta / 2

                new_date = ('Плановый срок устранения: ' + str(new_data)[8] + str(new_data)[9] + '.'
                            + str(new_data)[5] + str(new_data)[6] + '.'
                            + str(new_data)[0] + str(new_data)[1] + str(new_data)[2] + str(new_data)[3]
                            + b[36] + b[37] + b[38] + b[39] + b[40] + b[41] + b[42] + b[43] + b[44] + b[45] + b[46]
                            + b[47] + b[48] + b[49] + b[50] + b[51] + b[52] + b[53] + b[54])

                # Создает формат сообщения задачи
                task = [line[0], line[1], new_date, line[3], line[5], line[6]]

                # Конец стороннего кода


                # Создает формат сообщения задачи
                # task = [line[0], line[1], line[2], line[3], line[5], line[6]]

                # Фильтрует задачу по классу инцидента КТО
                if sort_direct.sort(task_inc, 'kto') == True:

                    # Фильтрует задачу по технику КТО
                    sort_tech.tech(task, numb_shop, 6, 'kto', k582, k117, k106, k344, k383, k980, 0, 0, 0, 0)

                # Фильтрует задачу по классу инцидента ФУЛЛ
                elif sort_direct.sort(task_inc, 'full') == True:

                    # Фильтрует задачу по технику ФУЛЛ
                    sort_tech.tech(task, numb_shop, 4, 'full', k502, k117, k472, k633, 0, 0, 0, 0, 0, 0)

                # Фильтрует задачу по классу инцидента New_conc
                elif sort_direct.sort(task_inc, 'new') == True:

                    # Фильтрует задачу по технику
                    sort_tech.tech(task, numb_shop, 4, 'new', k228, k117, k633, k344, 0, 0, 0, 0, 0, 0)

                else:
                    send_mess.take_mess(task, k128)


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
                    sort_tech.tech(inced, numb_shop, 4, 'full', k502, k117, k472, k633, 0, 0, 0, 0, 0, 0)

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