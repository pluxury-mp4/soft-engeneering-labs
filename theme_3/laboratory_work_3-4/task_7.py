# Задание 7. Манхэттенское расстояние
# Прогуливаясь по Манхэттену, вы не можете попасть из точки А в точку Б по кратчайшему пути. Если только вы не умеете проходить сквозь стены, вам обязательно придется идти вдоль его параллельно-перпендикулярных улиц.
# На плоскости манхэттенское расстояние между двумя точками (p1; p2) и (q1; q2) определяется так ∣p1−q1∣+∣p2−q2∣.
# Напишите программу, определяющую манхэттенское расстояние между двумя точками, координаты которых заданы.
p1 = int(input("Введите координату p1: "))
p2 = int(input("Введите координату p2: "))
q1 = int(input("Введите координату q1: "))
q2 = int(input("Введите координату q2: "))

manhattan_distance = abs(p1 - q1) + abs(p2 - q2)
print(manhattan_distance)
