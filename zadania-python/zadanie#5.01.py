class Material:

    rodzaj = ""
    dlugosc = 0
    szerokosc = 0

    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wyswietl_nazwe(self):
        print("Rodzaj materialu: ",self.rodzaj)

class Ubrania(Material):
    rozmiar = 0
    kolor = ""
    dla_kogo = ""

    def __init__(self, rodzaj, dlugosc, szerokosc, rozmiar, kolor, dla_kogo):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo

    def wyswietl_dane(self):
        print("Rozmiar: {}\nKolor: {}\nDla kogo: {}\n".format(self.rozmiar, self.kolor, self.dla_kogo))

class Sweter(Ubrania):
    rodzaj_swetra = ""

    def __init__(self, rodzaj, dlugosc, szerokosc, rozmiar, kolor, dla_kogo, rodzaj_swetra):
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo
        self.rodzaj_swetra = rodzaj_swetra

    def wyswietl_dane(self):
        print("Rozmiar: {}\nKolor: {}\nDla kogo: {}\nRodzaj swetra: {}\n".format(self.rozmiar, self.kolor, self.dla_kogo, self.rodzaj_swetra))
      

material = Material("kaszmir",10,20)
spodnie = Ubrania("jeans", 80, 40, "błękitne",'L' , "damskie")
nowy_sweter = Sweter("kaszmir",60, 45, 'M' ,"czarny", "męski","golf")
material.wyswietl_nazwe( )
print("\n")
spodnie.wyswietl_dane( )
print("\n")
nowy_sweter.wyswietl_dane()

