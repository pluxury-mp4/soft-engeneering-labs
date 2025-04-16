# Напишите программу, которая по номеру курса выводит информацию о данном курсе.

courses = {
    "CS101": {"room": "3004", "teacher": "Хайнс", "time": "8:00"},
    "CS102": {"room": "4501", "teacher": "Альварадо", "time": "9:00"},
    "CS103": {"room": "6755", "teacher": "Рич", "time": "10:00"},
    "NT110": {"room": "1244", "teacher": "Берк", "time": "11:00"},
    "CM241": {"room": "1411", "teacher": "Ли", "time": "13:00"}
}

course_number = input("Введите номер курса: ")
info = courses.get(course_number)
if info:
    print(f"{course_number}: {info['room']}, {info['teacher']}, {info['time']}")
else:
    print("Курс не найден.")