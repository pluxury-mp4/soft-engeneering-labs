# Задание 5. Следующее и предыдущее
#
# Напишите программу, которая считывает целое число, после чего на экран выводится следующее и предыдущее целое число с пояснительным текстом.
# Формат входных данных
# На вход программе подаётся целое число.
# Формат выходных данных
# Программа должна вывести текст согласно условию задачи.
num = int(input("Введите число: "))
print(f"Следующее число: {num + 1}")
print(f"Предыдущее число: {num - 1}")
