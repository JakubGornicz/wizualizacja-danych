class co_drugi:
    def __init__(self, data):
        self.i = 0
        self.step = 2
        self.end = len(str(data))
        self.data = str(data)
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.end:
            i = self.i
            self.i += self.step
            return self.data[i]
        else:
            raise StopIteration()

kolekcja = co_drugi("0123456789")
print(next(kolekcja))
print(next(kolekcja))
print(next(kolekcja))
print(next(kolekcja))
print(next(kolekcja))






