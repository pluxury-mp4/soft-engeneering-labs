# На вход программе подается строка текста. Напишите программу, которая выводит слова введенной строки в столбик.

text = input("Введите строку текста: ")
print("\n".join(text.split()))
