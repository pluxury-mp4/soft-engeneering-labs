# Напишите программу для вывода общего количества уникальных символов во всех считанных словах без учета регистра.

n = int(input("Введите количество слов: "))
unique_chars = set()

for _ in range(n):
    word = input("Введите слово: ")
    unique_chars.update(word.lower())

print(len(unique_chars))
