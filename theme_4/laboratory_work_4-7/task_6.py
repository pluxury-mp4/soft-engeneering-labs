# На вход программе подается строка текста, содержащая числа. Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.

numbers = input("Введите последовательность чисел через пробел: ").split()
seen = set()

for num in numbers:
    num = str(int(num))  # Убираем ведущие нули
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)
