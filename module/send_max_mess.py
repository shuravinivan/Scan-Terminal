import requests
from config import format_date
import time




# text = 'Удача с нами'
# chat_id = '-72298581395976'


def send_mess(text, chat_id):

    time.sleep(2)
    data = time.strftime(format_date)
    message = str(' '.join(text))
    print(data)
    print(message)

    from config import API
    from config import TOKEN_MAX
    from config import user_id

    r = requests.post(f"{API}/messages?chat_id={chat_id}",
                      headers={"Authorization": TOKEN_MAX, "Content-Type": "application/json"},
                      json={"text": f"{message}"})

    print('\n')

# send_mess(chat_id,text)