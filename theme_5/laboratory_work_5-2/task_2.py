# Проверка возможности перехода из документа A в документ B за два перехода.

import requests
from bs4 import BeautifulSoup

# Ввод URL документов A и B
url1 = input("Введите URL первого документа (A): ")
url2 = input("Введите URL второго документа (B): ")

# Функция для получения всех ссылок из HTML-документа
def get_links(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = [link.get('href') for link in soup.find_all('a') if link.get('href')]
            return links
        else:
            return []
    except:
        return []

# Получаем все ссылки из документа A
links_from_a = get_links(url1)

# Проверяем, можно ли перейти из A в B за два перехода
can_reach_b = False
for link in links_from_a:
    intermediate_links = get_links(link)
    if url2 in intermediate_links:
        can_reach_b = True
        break

# Вывод результата
print("Yes" if can_reach_b else "No")