# На вход программе подается число n, затем n строк с фамилией и оценкой ученика. Программа выводит всех учеников, затем хорошистов и отличников.

n = int(input("Введите количество учеников: "))
students = [input() for _ in range(n)]

for student in students:
    print(student)

print()

for student in students:
    if student.split()[1] in ("4", "5"):
        print(student)
