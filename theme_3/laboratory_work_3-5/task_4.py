# Задание 4. Тригонометрическое выражение
# Напишите программу, вычисляющую значение тригонометрического выражения sinx+cosx+tan2x по заданному числу градусов x.
import math

x = float(input("Введите угол в градусах: "))

x_rad = math.radians(x)

result = math.sin(x_rad) + math.cos(x_rad) + math.tan(x_rad)**2

print(f"Значение выражения: {result}")
