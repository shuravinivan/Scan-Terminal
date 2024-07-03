import schedule
import work_mail


def main():
    schedule.every(15).minutes.do(work_mail.mail)
    while True:
        schedule.run_pending()



if __name__ == "__main__":
    main()
