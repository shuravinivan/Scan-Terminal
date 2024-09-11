import mail_pars
import sort_direct
import sort_tech
import send_mess

def mail():

    # Техники КТО

        # ABAN = kto_tech_1 = Абашев_А
        # BUCT = kto_tech_2 = Булдаков_С
        # KUAL = kto_tech_3 = Кудрявцев_А
        # KUAN = kto_tech_4 = Кузнецов_А
        # FENI = kto_tech_5 = Федюнов_Н
        # SAGR = kto_tech_6 = Шадрин_Г
        # YFVA = kto_tech_7 = Юферов_В
        # NTKT = kto_tech_8 = НТ КТО

    # Техники ФУЛЛ

        # ABAN = full_tech_1 = Абашев_А
        # ZANI = full_tech_2 = Завьялов_Н
        # KUAL = full_tech_3 = Кудрявцев_А
        # KUAN = full_tech_4 = Кузнецов_А
        # MAAN = full_tech_5 = Малекин_А
        # NTFU = full_tech_6 = НТ ФУЛЛ

    # Техники Н.Концепт

        # ABAN = new_tech_1 = Абашев_А
        # KUAL = new_tech_2 = Кудрявцев_А
        # KUAN = new_tech_3 = Кузнецов_А
        # YDSE = new_tech_4 = Юданов_С
        # NTNC = new_tech_5 = НТ Н.Концепт

    # Каналы

    ABAN = '-1002167206495'
    BUCT = '-1002174436582'
    ZANI = '-1002135018502'
    KUAL = '-1002170795117'
    KUAN = '-1002149688633'
    MAAN = '-1002148412472'
    FENI = '-1002200909344'
    SAGR = '-1002228403383'
    YFVA = '-1002203331106'
    YDSE = '-1002163771228'
    NTKT = '-1002248392247'
    NTFU = '-1002163832980'
    NTNC = '-1002233608041'

    XXXX4 = '-1002210202214'

    # test = '-1002202663906'
    #
    # Gorev_A = test  # KTO (kto_tech_1)
    # Buldakob_S = test  # KTO (kto_tech_2)
    # Kuznecov_A = test  # KTO (kto_tech_3)
    # Malich_O = test  # KTO (kto_tech_4)
    # Abashev_A = test  # KTO (kto_tech_5)
    # Belich_A = test  # KTO (kto_tech_6)
    # Technic_K = test  # KTO (kto_tech_7)
    #
    # Zavyalov_N = test  # FULL (full_tech_1)
    # Malekin_A = test  # FULL (full_tech_2)
    # Kudravcev_A = test  # FULL (full_tech_3)
    # Technic_F = test  # FULL (full_tech_4)

    mail_name = "help_alexstroy@mail.ru"
    mail_pass = "09X7BYAayMx9vH7Lqu2t"

    while True:

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
                    sort_tech.tech(task, numb_shop, 8, 'kto', ABAN, BUCT, KUAL, KUAN, FENI, SAGR, YFVA, NTKT, 0, 0)

                # Фильтрует задачу по классу инцидента ФУЛЛ
                elif sort_direct.sort(task_inc, 'full') == True:

                    # Фильтрует задачу по технику ФУЛЛ
                    sort_tech.tech(task, numb_shop, 6, 'full', ABAN, ZANI, KUAL, KUAN, MAAN, NTFU, 0, 0, 0, 0)

                # Фильтрует задачу по классу инцидента New_conc
                elif sort_direct.sort(task_inc, 'new') == True:

                    # Фильтрует задачу по технику Coffee_Bread
                    sort_tech.tech(task, numb_shop, 5, 'new', ABAN, KUAL, KUAN, YDSE, NTNC, 0, 0, 0, 0, 0)

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
                sort_tech.tech(inced, numb_shop, 7, 'full', Zavyalov_N, Malekin_A, Kudravcev_A, Kuznecov_A, FULL_Sever, FULL_Izhevsk, Abashev_A, 0, 0, 0)



        else:
            print('Сообщений нет')
            break