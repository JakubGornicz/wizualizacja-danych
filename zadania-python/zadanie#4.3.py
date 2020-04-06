import sys

tresc = [ ]
with open("zadanie#4.3.py", "w+") as plik:
        for i in range(3):
            tresc.append(sys.stdin.readline( ))
        plik.writelines(tresc)
plik.close( )

print(tresc)
