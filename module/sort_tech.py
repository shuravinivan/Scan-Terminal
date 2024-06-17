import send_mess

#task - Ввод сообщения (Задача, Инцидент)
#num - Ввод строки для сравнения (Строка с содержанием номерв магазина)
#col - Количество абонентов (Количество техников направления, до 10 чел.)
#direct - Направление (КТО или ФУЛЛ)
#id_* - Номер чата техника



# Сортирует задачу по технику КТО
def Sort_tech(task, num, col, direct, id_1, id_2, id_3, id_4, id_5, id_6, id_7, id_8, id_9, id_10):

    for i in range(col):
        num_tech = i + 1
        direction = 'documents/' + direct + '_tech_' + str(num_tech) + '.txt'
        filter = open(direction, 'r', encoding='utf-8')
        sort = filter.read().splitlines()
        filter.close()
        for i in sort:
            num_call = num_tech
            abonent = i.strip()
            real_abonent = num[2].strip().replace(',', "")
            if real_abonent == abonent and num_call == 1:
                send_mess(task, id_1)
            elif real_abonent == abonent and num_call == 2:
                send_mess(task, id_2)
            elif real_abonent == abonent and num_call == 3:
                send_mess(task, id_3)
            elif real_abonent == abonent and num_call == 4:
                send_mess(task, id_4)
            elif real_abonent == abonent and num_call == 5:
                send_mess(task, id_5)
            elif real_abonent == abonent and num_call == 6:
                send_mess(task, id_6)
            elif real_abonent == abonent and num_call == 7:
                send_mess(task, id_7)
            elif real_abonent == abonent and num_call == 8:
                send_mess(task, id_8)
            elif real_abonent == abonent and num_call == 9:
                send_mess(task, id_9)
            elif real_abonent == abonent and num_call == 10:
                send_mess(task, id_10)
            else:
                continue
