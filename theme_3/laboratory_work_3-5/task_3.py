# Задание 3. Средние значения
import math

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

arithmetic_mean = (a + b) / 2
geometric_mean = math.sqrt(a * b)
harmonic_mean = 2 * a * b / (a + b)
quadratic_mean = math.sqrt((a**2 + b**2) / 2)

print(f"Среднее арифметическое: {arithmetic_mean}")
print(f"Среднее геометрическое: {geometric_mean}")
print(f"Среднее гармоническое: {harmonic_mean}")
print(f"Среднее квадратичное: {quadratic_mean}")
