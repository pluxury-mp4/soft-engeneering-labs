# Задача 7. Трехзначное число
# Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трёхзначного числа.
# Формат входных данных. На вход программе подаётся положительное трёхзначное число.
# Формат выходных данных. Программа должна вывести два числа с поясняющим текстом: сумма цифр и произведение цифр.
# Ввод: 123
num = int(input("Введите трёхзначное число: "))

a = num // 100
b = (num // 10) % 10
c = num % 10

print(f"Сумма цифр = {a + b + c}")
print(f"Произведение цифр = {a * b * c}")
