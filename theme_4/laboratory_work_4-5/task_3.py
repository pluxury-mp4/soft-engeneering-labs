# На вход программе подаётся число n и n×n элементов матрицы. Программа выводит след матрицы.

n = int(input("Введите размер матрицы: "))
matrix = [list(map(int, input().split())) for _ in range(n)]

print(sum(matrix[i][i] for i in range(n)))
