# Вам доступен текстовый файл population.txt с названиями стран и численностью их населения, разделенными символом табуляции '\t'.

file_name = "population.txt"

with open(file_name, 'r', encoding='utf-8') as file:
    for line in file:
        country, population = line.strip().split('\t')
        if country.startswith('G') and int(population) > 500000:
            print(country)