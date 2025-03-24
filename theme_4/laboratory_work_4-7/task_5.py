# Напишите программу для определения общего количества различных слов в строке текста.

import string

text = input("Введите строку текста: ").lower().translate(str.maketrans("", "", string.punctuation))
words = set(text.split())

print(len(words))
