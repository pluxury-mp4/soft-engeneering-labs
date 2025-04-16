# Напишите функцию func, используя синтаксис анонимных функций, которая принимает целочисленный аргумент и возвращает значение True, если он делится без остатка на 19 или на 13 и False в противном случае.

func = lambda x: x % 19 == 0 or x % 13 == 0

print(func(19))  # True
print(func(13))  # True
print(func(20))  # False
print(func(15))  # False
print(func(247))  # True