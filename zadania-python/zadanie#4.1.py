import random

arr = [ ]
for i in range(4):
    arr.append(random.randint(4,10)*4)

plik = open("zadanie#4.1.py","a+")
plik.writelines(str(arr))
plik.close()
