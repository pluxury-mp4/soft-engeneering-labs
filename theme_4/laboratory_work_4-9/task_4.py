# Дополните приведенный код, чтобы в переменной result хранился словарь, в котором ключи – числа от 1 до 15 (включительно), а значения представляют собой квадраты ключей.

result = {}
for i in range(1, 16):
    result[i] = i ** 2
print(result)