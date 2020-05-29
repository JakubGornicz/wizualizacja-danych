import numpy as np

# Napisz funkcję, która:
# - na wejściu przyjmuje jeden parametr określający długość wektora,
# - na podstawie parametru generuje wektor, ale w kolejności
#    odwróconej (czyli np. dla n=3 =>[3 2 1])
# - generuje macierz diagonalną z w/w wektorem jako przekątną

def funkcja(dlugosc) :
    a = np.arange(1, dlugosc+1)
    a = np.flip(a)
    print("Wektor:", a)

    mat = np.zeros((dlugosc, dlugosc))
    mat = np.diag([i for i in a])
    print("Macierz:\n", mat)
    

funkcja(4)
