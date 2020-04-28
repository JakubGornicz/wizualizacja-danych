import itertools


kombinacja = itertools.combinations('0123456789', 3)
for i in itertools.combinations('0123456789', 3):
    print(next(kombinacja))
