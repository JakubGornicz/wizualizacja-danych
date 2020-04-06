#Napisz skrypt, który pobiera od użytkownika dwie wartości i mnoży je przez siebie. Wynik wyświetla
#na ekranie (użyj instrukcji readline() i write()).

import sys


print("Podaj pierwsza wartość: ")
a = float(sys.stdin.readline())
print("Podaj drugą wartość: ")
b = float(sys.stdin.readline())
sys.stdout.write(str(a*b))
