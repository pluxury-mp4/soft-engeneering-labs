# На вход программе подается число n. Программа выводит первые n чисел последовательности Трибоначчи.

n = int(input("Введите количество чисел последовательности: "))
tribonacci = [1, 1, 1]

for i in range(3, n):
    tribonacci.append(tribonacci[i - 1] + tribonacci[i - 2] + tribonacci[i - 3])

print(*tribonacci[:n])
