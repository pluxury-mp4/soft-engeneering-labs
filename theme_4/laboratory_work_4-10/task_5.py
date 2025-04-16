# Напишите программу с использованием встроенной функции all() для проверки корректности IP-адреса: все ли октеты в IP-адресе – числа со значением от 0 до 255.

ip_address = input("Введите IP-адрес: ")
octets = ip_address.split('.')

is_valid = all(octet.isdigit() and 0 <= int(octet) <= 255 for octet in octets)

print(is_valid)