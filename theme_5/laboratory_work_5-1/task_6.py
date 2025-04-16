# Вам доступен текстовый файл logfile.txt с информацией о времени входа пользователя в систему и выхода из нее.

from datetime import datetime

def time_difference(start_time, end_time):
    fmt = "%H:%M"
    start = datetime.strptime(start_time, fmt)
    end = datetime.strptime(end_time, fmt)
    diff = (end - start).seconds // 60
    return diff >= 60

input_file = "logfile.txt"
output_file = "output.txt"

with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    for line in infile:
        name, login, logout = line.strip().split(', ')
        if time_difference(login, logout):
            outfile.write(name + '\n')