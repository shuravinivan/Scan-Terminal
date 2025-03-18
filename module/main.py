import schedule
import work_mail


def main():
    print('Good afternoon!')
    print('Scan Terminal online.')
    schedule.every(10).minutes.do(work_mail.mail)
    while True:
        schedule.run_pending()

if __name__ == "__main__":
    main()
