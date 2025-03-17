# На вход программе подаётся число n и n×n элементов матрицы. Программа выводит максимальный элемент в заштрихованной области.

n = int(input("Введите размер матрицы: "))
matrix = [list(map(int, input().split())) for _ in range(n)]

print(max(matrix[i][j] for i in range(n) for j in range(n) if i <= j or i + j >= n - 1))
