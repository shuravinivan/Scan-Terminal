#task - Ввод сообщения (Задача, Инцидент)
#dir - Направление (КТО или ФУЛЛ)

def sort_shop(task, dir):

    # Фильтрует задачу по классу инцидента КТО
    direction = 'documents/' + 'filter_' + dir + '.txt'
    filter = open(direction, 'r', encoding='utf-8')
    sort = filter.read().splitlines()
    filter.close()
    for el_str in sort:
        task_inc = task[4]
        line = el_str
        if task_inc.strip() == line.strip():
            klass_inc = True

    return klass_inc