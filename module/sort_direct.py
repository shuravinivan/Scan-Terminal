import time
from config import format_date
#task - Ввод сообщения (Задача, Инцидент)
#direct - Направление (КТО или ФУЛЛ)

def sort(task_inc, direct):

    # Фильтрует задачу по классу инцидента КТО
    try:
        filter = open('../documents/' + 'filter_' + direct + '.txt', 'r', encoding='utf-8')
        sort = filter.read().splitlines()
        filter.close()
        for el_str in sort:
            if task_inc.strip() == el_str.strip():
                klass_inc = True
                return klass_inc
    except:
        print(time.strftime(format_date))
        print('Ошибка модуля sort_direct', '\n')