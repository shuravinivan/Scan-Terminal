import time
import requests
import config_token

def take_mess(mess, id):
    time.sleep(5)
    data = time.strftime('%d/%m/%Y %H:%M')
    print(data)
    TOKEN = config_token.TOKEN
    chat_id = id
    message = str(' '.join(mess))
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json())  # Эта строка отсылает сообщение
    print('\n')