plik = open("zadanie#4.1.py", "r")
linia = plik.readline()
with open("zadanie#4.1.py", "r") as plik:
    for linia in plik:
        print(linia, end="")
