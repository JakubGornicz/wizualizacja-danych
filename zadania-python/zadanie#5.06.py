imie = "Reks"
it = iter(imie)
print(it)
# na wyjściu: <str_iterator object at 0x0000000003807FD0>
next(it)
# 'R'
next(it)
# 'e'
next(it)
# 'k'
next(it)
# 's'


lista = ["jeden", "dwa", "trzy"]
l = iter(lista)
print(next(l))
print(next(l))
print(next(l))
print("\n")
tuple = (1, 3, 6, 2)
t = iter(tuple)
print(next(t))
print(next(t))
print(next(t))
print(next(t))

