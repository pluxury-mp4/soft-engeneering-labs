# 2.1. Загружаем сохраненные массивы из файла
import numpy as np

data = np.load("weather_data.npz")
dates = data['dates']
temperatures = data['temperatures']

# 2.2. Находим минимальную и максимальную температуру за год
min_temp = temperatures[:, 0].min()  # Минимальная температура (столбец tmin)
max_temp = temperatures[:, 1].max()  # Максимальная температура (столбец tmax)

# 2.3. Находим даты для соответствующих температур
min_temp_date_index = temperatures[:, 0].argmin()
max_temp_date_index = temperatures[:, 1].argmax()

min_temp_date = dates[min_temp_date_index]
max_temp_date = dates[max_temp_date_index]

# Выводим результаты
print(f"Минимальная температура за год: {min_temp}°C, дата: {min_temp_date}")
print(f"Максимальная температура за год: {max_temp}°C, дата: {max_temp_date}")