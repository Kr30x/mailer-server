
import dotenv
import os
import requests

def send_message(message: str) -> str:
    dotenv.load_dotenv()
    TOKEN = os.getenv("TOKEN")
    ADMIN_ID = os.getenv("ADMIN_ID")
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    params = {
        'chat_id': ADMIN_ID,
        'text': message
    }
    response = requests.post(url, params=params)
    return response.json()
