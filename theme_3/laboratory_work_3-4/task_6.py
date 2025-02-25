# Задание 6. Сортировка трёх
# Напишите программу, которая упорядочивает три числа от большего к меньшему.

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

sorted_numbers = sorted([a, b, c], reverse=True)
for num in sorted_numbers:
    print(num)
