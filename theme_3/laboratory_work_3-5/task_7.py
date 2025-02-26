# Задание 7. Правильный многоугольник.
# Даны два числа: натуральное число n и вещественное число a. Напишите программу, которая находит площадь указанного правильного многоугольника.
import math

n = int(input("Введите количество сторон: "))
a = float(input("Введите длину стороны: "))

area = (n * a**2) / (4 * math.tan(math.pi / n))

print(f"Площадь правильного многоугольника: {area}")
