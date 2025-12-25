# import schedule
import work_mail
import time
from config import format_date


def main():
    data = time.strftime(format_date)
    print('\n' + 'Добрый день! Сканер терминала вер.1.8.10 активен. ' + data + '\n')
    # schedule.every(10).minutes.do(work_mail.mail)
    while True:
        work_mail.mail()
        time.sleep(600)
        # schedule.run_pending()

if __name__ == "__main__":
    main()
