# Задание 5. Повторяй за мной
# Напишите программу, которая считывает три строки по очереди, а затем выводит их в обратной последовательности, каждую на отдельной строчке.
# Формат входных данных
# На вход программе подается три строки, каждая на отдельной строке.
# Формат выходных данных
# Программа должна вывести введенные строки в обратной последовательности, каждую на отдельной строке.
# Примечание. Используйте 3 переменные для сохранения введённых строк текста.
first_line = input('Введите значение первой строки: ')
second_line = input('Введите значение второй строки: ')
third_line = input('Введите значение третьей строки: ')
print(third_line, second_line, first_line, sep="\n")