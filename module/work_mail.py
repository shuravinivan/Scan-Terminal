import mail_pars
import sort_direct
import sort_tech
import send_mess

def mail():
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

    # mail_name = "test-alexstroy@mail.ru" # Тест почта
    # mail_pass = "BGBLZdH6gbCQyTtY9PYv" # Тест пароль

    Test = '-1002202663906'

    Gorev_A = Test #KTO (kto_tech_1)
    Buldakob_S = Test #KTO (kto_tech_2)
    Kuznecov_A = Test #KTO (kto_tech_3)
    Malich_O = Test #KTO (kto_tech_4)
    Abashev_A = Test #KTO (kto_tech_5)
    Belich_A = Test #KTO (kto_tech_6)
    Technic_K = Test #KTO (kto_tech_7)

    Zavyalov_N = Test #FULL (full_tech_1)
    Malekin_A = Test #FULL (full_tech_2)
    Kudravcev_A = Test #FULL (full_tech_3)
    Technic_F = Test #FULL (full_tech_4)

    mail_name = "help_alexstroy@mail.ru"
    mail_pass = "09X7BYAayMx9vH7Lqu2t"

    letter = mail_pars.mail(mail_name, mail_pass)
    if letter != None:
        title = (letter.split('\n')[0]).split()

        # Сортирует задачи
        if title[0] == 'Зарегистрирована' and title[1] == 'новая' and title[2] == 'задача':

            # Создает переменные строк
            line = letter.split('\n')
            numb_shop = ((line[3].split()[2]).replace(',', ''))
            task_inc = line[5]

            # Создает формат сообщения задачи
            task = [line[0], line[1], line[2], line[3], line[5], line[6]]

            # Фильтрует задачу по классу инцидента КТО
            if sort_direct.sort(task_inc, 'kto') == True:

                # Фильтрует задачу по технику КТО
                sort_tech.tech(task, numb_shop, 7, 'kto', Gorev_A, Buldakob_S, Kuznecov_A, Malich_O, Abashev_A, Belich_A, Technic_K, 0, 0, 0)

            # Фильтрует задачу по классу инцидента ФУЛЛ
            elif sort_direct.sort(task_inc, 'full') == True:

                # Фильтрует задачу по технику ФУЛЛ
                sort_tech.tech(task, numb_shop, 4, 'full', Zavyalov_N, Malekin_A, Kudravcev_A, Technic_F, 0, 0, 0, 0, 0, 0)
            else:
                send_mess.take_mess(task, '-1002243705128')

        # Сортирует ициденты
        elif title[0] == 'Зарегистрирован' and title[1] == 'инцидент,':  # Фильтр ицидентов

            # Создает переменные строк
            line = letter.split('\n')
            numb_shop = (((((line[4]).split())[1]).replace('_', ' ')).split())[1]

            # Создает формат сообщения инцидента
            inced = [line[0], line[1], line[2], line[4], line[5], line[6], line[7], line[8], line[9], line[10]]

            # Фильтрует задачу по технику ФУЛЛ
            sort_tech.tech(inced, numb_shop, 4, 'full', Zavyalov_N, Malekin_A, Kudravcev_A, Technic_F, 0, 0, 0, 0, 0, 0)



    else:
        print('Сообщений нет')