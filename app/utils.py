import threading
import time
from mistralai import Mistral
from config import API_KEY


def mistral(message):
    """Вызывает API Mistral с таймаутом."""
    timeout = 60
    client = Mistral(api_key=API_KEY)
    model_name = "mistral-medium-2505"

    result = [None]  # Используем список, чтобы изменить его внутри потока

    def call_api():
        try:
            response = client.chat.complete(
                model=model_name,
                messages=message
            )
            result[0] = response.choices[0].message.content
        except Exception as e:
            print(f"Ошибка API: {e}")

    thread = threading.Thread(target=call_api)
    thread.start()
    thread.join(timeout)  # Ждем `timeout` секунд

    if thread.is_alive():
        return None

    time.sleep(30)
    return str(result[0]) if result[0] else None
