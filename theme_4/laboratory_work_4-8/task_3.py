# На вход программе подаются два числа. Напишите программу, определяющую, есть ли в данных числах одинаковые цифры.

num1 = input("Введите первое число: ")
num2 = input("Введите второе число: ")

if set(num1) & set(num2):
    print("YES")
else:
    print("NO")