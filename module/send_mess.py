import time
import requests

def take_mess(mess, id):
    time.sleep(5)
    TOKEN = "7240204692:AAHiUSc0DdlcN2YEZsj-xbLgc9EqCpkMV1Q"
    chat_id = id
    message = str(' '.join(mess))
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json())  # Эта строка отсылает сообщение