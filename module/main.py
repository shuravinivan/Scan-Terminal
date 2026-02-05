import work_mail
import time
from config import format_date
from config import version

try:
    def main():
        data = time.strftime(format_date)
        print('\n' + data + ' ' + 'Добрый день! Сканер терминала' + version + 'активен. ' + '\n')

        while True:
            work_mail.mail()
            time.sleep(600)

except:
    print(time.strftime(format_date))
    print('Внутренняя ошибка')

if __name__ == "__main__":
    main()
