import time
import requests
from config import TOKEN
from config import format_date

def take_mess(mess, id):
    time.sleep(5)
    data = time.strftime(format_date)
    print(data)
    key = TOKEN
    chat_id = id
    message = str(' '.join(mess))
    url = f"https://api.telegram.org/bot{key}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json())  # Эта строка отсылает сообщение
    print('\n')