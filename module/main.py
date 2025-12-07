# import schedule
import work_mail
import time


def main():
    data = time.strftime('%d/%m/%Y %H:%M')
    print('\n' + 'Добрый день! Сканер терминала активен. ' + data + '\n')
    # schedule.every(10).minutes.do(work_mail.mail)
    while True:
        work_mail.mail()
        time.sleep(600)
        # schedule.run_pending()

if __name__ == "__main__":
    main()
