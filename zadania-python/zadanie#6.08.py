import numpy as np
# Napisz funkcję, która:
# - jako parametr wejściowy będzie przyjmowała tablicę wielowymiarową
#    numpy oraz parametr ‘kierunek’,
# - parametr kierunek określa czy tablica wejściowa będzie dzielona
#    w pionie czy poziomie
# - funkcja dzieli tablicę wejściową na pół (napisz warunek, który
#    wyświetli komunikat, że ilość wierszy lub kolumn, w zależności
#    od kierunku podziału, nie pozwala na operację)

pion = 1
poziom = 0
def podziel(tablica, kierunek) :
    wiersze, kolumny = tablica.shape
    if kierunek == 1 :
        if kolumny%2 == 0 :
            print("Dzielenie pionowe:\n",np.hsplit(tablica, 2)[0],"\n"*2,np.hsplit(tablica, 2)[1])
        else :
            print("Tablica zawiera nieparzysą liczbę kolumn...")

    elif kierunek == 0 :
        if wiersze%2 == 0 :
            print("Dzielenie poziome:\n",np.split(tablica, 2)[0],"\n"*2,np.split(tablica, 2)[1])
        else :
            print("Tablica zawiera nieparzysą liczbę wierszy...")

a = np.array([ [1,2,3,4],[5,6,7,8] ])
print("Tablica przed funkcją:\n",a,"\n")
podziel(a, 1)
podziel(a, 0)
b = np.array([ [1,2,3],[5,6,7],[8,9,10] ])
print("Tablica przed funkcją:\n",b,"\n")
podziel(b, 1)
podziel(b, 0)
