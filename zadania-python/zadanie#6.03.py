import numpy as np

# Napisz funkcję, która będzie:
# - przyjmowała jeden parametr ‘n’ w postaci liczby całkowitej
# - zwracała tablicę Numpy o wymiarach n*n kolejnych
#    liczb całkowitych poczynając od 1

n = int(input("Podaj liczbę całkowitą: "))

a = np.arange(1, pow(n,2)+1)
a = a.reshape((n, n))
print(a)

