import numpy as np

# Stwórz skrypt który na wyjściu wyświetli macierz numpy
# (tablica wielowymiarowa) w postaci wykreślanki, gdzie jedno słowo
# będzie wypisane w kolumnie, jedno w wierszu i jedno po ukosie.
# Jedno z tych słów powinno być wypisane od prawej do lewej.

imiona = ["sebastian", "małgorzata", "alfred"]
dl_max= ""
krotsze = []
for i in imiona :
    if len(i) > len(dl_max) :
        dl_max = i
for i in imiona :
    if len(i) < len(dl_max) :
        krotsze.append(i)
        
mat = np.diag([a for a in dl_max])
mat = np.flip(mat)
for i in range(len(krotsze[0])) :
    mat[0][i+1] = krotsze[0][i]
for i in range(len(krotsze[1])) :
    mat[i+1][0] = krotsze[1][i]
print(mat)

