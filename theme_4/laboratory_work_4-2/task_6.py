# На вход программе подается натуральное число n, затем n строк, затем еще одна строка — поисковый запрос. Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.

n = int(input("Введите количество строк n: "))
lines = [input(f"Введите строку {i + 1}: ") for i in range(n)]
query = input("Введите поисковый запрос: ").lower()
print("\n".join(line for line in lines if query in line.lower()))
