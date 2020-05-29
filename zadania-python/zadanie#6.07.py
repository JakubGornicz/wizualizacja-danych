import numpy as np

# Napisz funkcję, która wygeneruje macierz wielowymiarową postaci:
# [[2 4 6]
#  [4 2 4]
#  [6 4 2]]
# Przy założeniach:
# - funkcja przyjmuje parametr n, który określa wymiary macierzy
# jako n*n i umieszcza wielokrotność liczby 2 na kolejnych jej przekątnych
# rozchodzących się od głównej przekątnej.

def funkcja(n) :
    mat = np.full((n,n), 2)
    wart_2 = 2
    for i in range(1, n) :
        mat[0][i] += wart_2
        mat[i][0] += wart_2

        wart_2 += 2
        
        
        
        
        
    print(mat)
        
    

funkcja(4)
