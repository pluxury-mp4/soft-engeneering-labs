import requests
import numpy as np
from datetime import datetime

# 1.4. Получаем код ближайшей метеорологической станции для Воронежа
# Координаты Воронежа: 51.6720, 39.1843
nearby_stations_url = "https://meteostat.p.rapidapi.com/stations/nearby"
headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",  # Замените на ваш API-ключ
    "X-RapidAPI-Host": "meteostat.p.rapidapi.com"
}
querystring = {"lat": "51.6720", "lon": "39.1843"}

response = requests.get(nearby_stations_url, headers=headers, params=querystring)
print(response.text)  # Выводим полный ответ сервера
station_data = response.json()

# Берем ID первой станции из списка
station_id = station_data['data'][0]['id']
print(f"ID станции: {station_id}")

# 1.5. Делаем запрос за историческими данными погоды
daily_station_url = "https://meteostat.p.rapidapi.com/stations/daily"
start_date = "2021-01-01"
end_date = "2021-12-31"

querystring = {
    "station": station_id,
    "start": start_date,
    "end": end_date
}

response = requests.get(daily_station_url, headers=headers, params=querystring)
weather_data = response.json()

# 1.6. Парсим данные
dates = []
temperatures = []

for day in weather_data['data']:
    date = day['date']
    tmin = day['tmin']  # Минимальная температура
    tmax = day['tmax']  # Максимальная температура
    tavg = day['tavg']  # Средняя температура

    dates.append(date)
    temperatures.append([tmin, tmax, tavg])

# Преобразуем в numpy массивы
dates_array = np.array(dates)
temperatures_array = np.array(temperatures)

# 1.7. Сохраняем массивы в файл
np.savez_compressed("weather_data.npz", dates=dates_array, temperatures=temperatures_array)
print("Данные сохранены в файл 'weather_data.npz'")