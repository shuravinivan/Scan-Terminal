import imaplib
import email
import base64
import time
from config import format_date

# Работает с почтой mail.ru
# Получает только не прочитанные письма

#Получает почту
def mail (mail_name, mail_pass):

    try:
        # Вход на сервер почты
        imap_server = "imap.mail.ru"
        imap = imaplib.IMAP4_SSL(imap_server)
        imap.login(mail_name, mail_pass)

        # Переход во входящие
        imap.select("INBOX")

        # Получает порядковые номера непрочитанных писем и записывает в переменную
        list_unread = imap.search(None, "UNSEEN")
        list_unread = list_unread[-1][0]
        list_unread = list_unread.split()
        num_letter = len(list_unread)

        # Условия для проверки непрочитанных писем
        if num_letter != 0:


            # Получает и обрабатывает почту
            for letter_num in list_unread:

                # Получает письмо по порядковому номеру и извлекает содержимое
                res, msg = imap.fetch(letter_num, '(RFC822)')  # Получение письма по порядковому номеру
                msg = email.message_from_bytes(msg[0][1])  # Извлекает содержимое письма

                # Извлекает текст письма из содержимого и записывает в переменную
                for part in msg.walk():
                    if part.get_content_maintype() == 'text' and part.get_content_subtype() == 'plain':
                        letter = base64.b64decode(part.get_payload()).decode(encoding='utf-8', errors='ignore')
                        # letter = letter_iso.encode('ISO-8859-1').decode('cp1251', errors='ignore')

                        return letter

        # Выход с почтового сервера
        imap.close()
        imap.logout()

    except:
        print(time.strftime(format_date))
        print('Нет соединения!', '\n')