# На вход программе подаются числа n и m. Программа выводит таблицу умножения размером n×m.

n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

for i in range(n):
    print(*(str(i * j).ljust(3) for j in range(m)))
