# На вход программе подается строка с именем текстового файла. Напишите программу, которая выводит на экран его предпоследнюю строку.

file_name = input("Введите имя файла: ")

with open(file_name, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print(lines[-2].strip())