import schedule
import work_mail
import time


def main():
    print('Добрый день!' + '\n' + 'Терминал активен.' + '\n')
    # schedule.every(10).minutes.do(work_mail.mail)
    # work_mail.mail()
    # time.sleep(600)
    while True:
        work_mail.mail()
        time.sleep(600)
        # schedule.run_pending()

if __name__ == "__main__":
    main()
