# На вход программе подаются числа n и m, затем n×m слов. Программа выводит матрицу, затем пустую строку, затем транспонированную матрицу.

n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
matrix = [input() for _ in range(n * m)]

for i in range(n):
    print(*matrix[i * m:(i + 1) * m])

print()

for j in range(m):
    print(*[matrix[i * m + j] for i in range(n)])
