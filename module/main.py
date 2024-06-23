import schedule
import work_mail


def main():
    schedule.every(5).seconds.do(work_mail.mail)
    while True:
        schedule.run_pending()



if __name__ == "__main__":
    main()
