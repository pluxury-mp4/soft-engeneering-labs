import numpy as np

# 2.1. Создать массив из 10 элементов типа uint16, состоящий из нулей
array_zeros = np.zeros(10, dtype=np.uint16)
print("Массив из нулей:", array_zeros)

# 2.2. Создать массив того же размера и типа, состоящий из двоек
array_twos = np.full(10, 2, dtype=np.uint16)
print("Массив из двоек:", array_twos)

# 2.3. Создать массив из чисел от 10 до 15 с шагом 0.5 типа float32
array_range = np.arange(10, 15.5, 0.5, dtype=np.float32)
print("Массив от 10 до 15 с шагом 0.5:", array_range)

# 2.4. Создать массив случайных чисел (randn), из него создать ещё один массив, в который попадёт выборка отрицательных элементов
random_array = np.random.randn(10)  # Массив из 10 случайных чисел
negative_elements = random_array[random_array < 0]  # Выборка отрицательных элементов
print("Массив случайных чисел:", random_array)
print("Выборка отрицательных элементов:", negative_elements)