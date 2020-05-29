import numpy as np

# Napisz funkcję, która będzie przyjmowała 2 parametry: liczbę, która
# będzie podstawą operacji potęgowania oraz ilość kolejnych potęg
# do wygenerowania. Korzystając z funkcji logspace generuj tablicę
# jednowymiarową kolejnych potęg
# podanej liczby, np. generuj(2,4) -> [2 4 8 16]


def generuj(podstawa, ilosc) :
    potegi = np.logspace(1, ilosc, base=podstawa, num=ilosc , dtype="int64")
    print(potegi)
    
podstawa = int(input("Podaj podstawę potęgi: "))
ilosc = int(input("Podaj ile liczb chcesz wygenerować: "))

generuj(podstawa, ilosc)    
