# Напишите программу для вывода количества уникальных символов каждого считанного слова без учета регистра.

n = int(input("Введите количество слов: "))

for _ in range(n):
    word = input("Введите слово: ")
    print(len(set(word.lower())))
