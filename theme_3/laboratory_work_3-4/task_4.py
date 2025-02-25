# Задание 4. Первая цифра после точки
# Дано положительное действительное число. Выведите его первую цифру после десятичной точки.
num = float(input("Введите число: "))

fractional_part = num % 1
first_digit = int(fractional_part * 10)
print(first_digit)
