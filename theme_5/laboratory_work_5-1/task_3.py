# Вам доступен текстовый файл prices.txt с информацией о заказе из интернет-магазина. В нем каждая строка разделена на три колонки: наименование товара, количество товара (целое число), цена за 1 шт (целое число).

file_name = "prices.txt"

with open(file_name, 'r', encoding='utf-8') as file:
    total_cost = 0
    for line in file:
        product, quantity, price = line.strip().split('\t')
        total_cost += int(quantity) * int(price)

print(total_cost)