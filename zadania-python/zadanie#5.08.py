class samogloski:
    def __init__(self, data):
        self.i = 0
        self.data = data
        self.end = len(str(data))
        self.vowels = "aeiou"

    def __iter__(self):
        return self

    def wyswietl_dane(self):
        return self.data
    
    def __next__(self):
        i = self.i
        if self.i < self.end and self.data[i] in self.vowels :
            self.i += 1
            return self.data[i]
        elif self.i < self.end and self.data[i] not in self.vowels :
            self.i +=1
            return ""
        else:
            raise StopIteration()

wyraz = samogloski("aagbeeupixieololul")
print("Czy objekt 'wyraz' jest instancją klasy samogloski?: ", isinstance(wyraz, samogloski))
print("Pierwotny wyraz:",wyraz.wyswietl_dane( ))
print("Stosując iterator:",end=" ")
print(next(wyraz), end="")
print(next(wyraz), end="")
print(next(wyraz), end="")
print(next(wyraz), end="")
print(next(wyraz), end="")
print(next(wyraz), end="")
print(next(wyraz), end="")
print(next(wyraz), end="")
print(next(wyraz), end="")
print(next(wyraz), end="")
print(next(wyraz), end="")
print(next(wyraz), end="")
print(next(wyraz), end="")
print(next(wyraz), end="")
print(next(wyraz), end="")
print(next(wyraz), end="")
print(next(wyraz), end="")
print(next(wyraz), end="")


