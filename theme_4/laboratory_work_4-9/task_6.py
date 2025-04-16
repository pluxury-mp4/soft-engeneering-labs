# Напишите программу для расшифровки секретного слова методом частотного анализа.

encrypted_word = input("Введите зашифрованное слово: ")
n = int(input("Введите количество букв в словаре: "))

frequency = {}
for _ in range(n):
    letter, count = input().split(": ")
    frequency[int(count)] = letter

decrypted_word = ''.join(frequency[encrypted_word.count(char)] for char in encrypted_word)
print(decrypted_word)