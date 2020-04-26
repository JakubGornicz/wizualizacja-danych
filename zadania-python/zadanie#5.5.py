class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        # lub
        # super().__init__(imie, nazwisko)
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


class Menadzer(Pracownik):

    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


jozek = Pracownik("Józek", "Bajka", 2000)
adrian = Menadzer("Adrian", "Mikulski", 12000)

print(jozek.przedstaw_sie())
print(adrian.przedstaw_sie())

print('Czy objekt "jozek"jest instancja klasy Osoba: ', isinstance(jozek, Osoba))
print('Czy objekt "jozek"jest instancja klasy Pracownik: ', isinstance(jozek, Pracownik))
print('Czy objekt "jozek"jest instancja klasy Menadzer: ', isinstance(jozek, Menadzer))
print("\n")
print('Czy objekt "adrian"jest instancja klasy Osoba: ', isinstance(adrian, Osoba))
print('Czy objekt "adrian"jest instancja klasy Pracownik: ', isinstance(adrian, Pracownik))
print('Czy objekt "adrian"jest instancja klasy Menadzer: ', isinstance(adrian, Menadzer))
print("\n")
print('Czy klasa Pracownik jest podklasa klasy Osoba: ', issubclass(Pracownik, Osoba))
print('Czy klasa Menadzer jest podklasa klasy Osoba: ', issubclass(Menadzer, Osoba))
print('Czy klasa Menadzer jest podklasa klasy Pracownik: ', issubclass(Menadzer, Pracownik))

