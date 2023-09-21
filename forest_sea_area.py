import numpy as np
import random

# Tworzenie macierzy 4x4
matrix = np.empty((4, 4), dtype=object)

# Wypełnianie macierzy losowymi liczbami i jedną z trzech liter: 'W', 'L' lub 'M'
for i in range(4):
    for j in range(4):
        random_number = random.randint(2, 20)  # Losowa liczba z przedziału [2, 20)
        random_letter = random.choice(['W', 'L', 'M'])  # Losowanie jednej z trzech liter
        matrix[i, j] = f"{random_number}, {random_letter}"

# Wyświetlanie macierzy

print(matrix)