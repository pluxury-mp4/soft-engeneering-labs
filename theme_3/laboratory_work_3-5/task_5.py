# Задание 5. Пол и потолок
# Напишите программу, вычисляющую значение ⌈x⌉ +⌊x⌋ по заданному вещественному числу x.

import math

x = float(input("Введите число: "))
result = math.ceil(x) + math.floor(x)
print(f"Сумма потолка и пола числа: {result}")

