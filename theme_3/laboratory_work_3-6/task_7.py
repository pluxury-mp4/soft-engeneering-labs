# Задание 7. Гласные и согласные
# На вход программе подается одна строка с буквами русского языка. Напишите программу, которая определяет количество гласных и согласных букв.
text = input("Введите строку: ").lower()

vowels = "ауоыиэяюёе"
consonants = "бвгджзйклмнпрстфхцчшщ"

vowel_count = sum(1 for char in text if char in vowels)
consonant_count = sum(1 for char in text if char in consonants)

print(f"Количество гласных букв равно {vowel_count}")
print(f"Количество согласных букв равно {consonant_count}")
