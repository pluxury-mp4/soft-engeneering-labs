# Задание 2. Повторяй за мной 1
# Дано предложение и количество раз, которое его надо повторить. Напишите программу, которая повторяет данное предложение нужное количество раз.
sentence = input("Введите предложение: ")
repeats = int(input("Введите количество повторений: "))

for _ in range(repeats):
    print(sentence)
