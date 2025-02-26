# Задание 2. Площадь и длина
# Напишите программу определяющую площадь круга и длину окружности по заданному радиусу R.
import math

R = float(input("Введите радиус: "))

area = math.pi * R ** 2
circumference = 2 * math.pi * R

print(f"Площадб: {area}")
print(F"Длинна окружности: {circumference}")
