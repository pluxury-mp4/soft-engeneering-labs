# Простая задача на get запрос и проверку ответа.

import requests

url = input("Введите URL: ")

response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print(f"Упс, произошла ошибка!..\nКод ошибки - {response.status_code}")