# На вход программе подается строка текста, содержащая различные натуральные числа.
# Напишите программу, которая меняет местами минимальный и максимальный элемент этого списка.

numbers = list(map(int, input("Введите последовательность различных чисел через пробел: ").split()))
min_idx, max_idx = numbers.index(min(numbers)), numbers.index(max(numbers))
numbers[min_idx], numbers[max_idx] = numbers[max_idx], numbers[min_idx]
print(" ".join(map(str, numbers)))
