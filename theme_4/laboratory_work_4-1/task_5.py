# Задание 5. Переворот
# На вход программе подается строка текста, в которой буква «h» встречается как минимум два раза. Напишите программу, которая возвращает исходную строку и переворачивает последовательность символов, заключенную между первым и последним вхождением буквы «h».
text = input("Введите строку, содержащую минимум две буквы 'h': ")
first_index = text.find('h')
last_index = text.rfind('h')
result = text[:first_index + 1] + text[first_index + 1:last_index][::-1] + text[last_index:]
print(f"Результат: {result}")
