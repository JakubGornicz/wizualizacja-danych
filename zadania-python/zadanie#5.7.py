class Parzyste:

  def __init__(self, data):
        self.data = k
        self.start = 2
        self.end = len(data)
  def __iter__(self):
        return self

  def __next__(self):
        if self.end == 0:
            raise StopIteration
        self.start = self.start + 2
        return self.data[self.start]

kolekcja = ["dum", "du", "dum","du","dum","du", "dum","du", "dum","du", "dum","du", "dum","du", "dum","du"]
k = iter(kolekcja)
supa = Parzyste(kolekcja)
print(next(k))
print(next(k))




