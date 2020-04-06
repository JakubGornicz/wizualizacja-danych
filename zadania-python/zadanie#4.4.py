class NaZakupy :

        def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed) :
               self.nazwa_produktu = nazwa_produktu
               self.ilosc = ilosc
               self.jednostka_miary = jednostka_miary
               self.cena_jed = cena_jed

        def wyswietl_produkt(self) :
               print(f"Nazwa: {self.nazwa_produktu}\nIlość: {self.ilosc}\nJednostka: {self.jednostka_miary}\nCena: {self.cena_jed}zł")

        def ile_produktu(self) :
               print(self.ilosc, self.jednostka_miary)

        def ile_kosztuje(self, ile) :
              return self.cena_jed*ile

ziemniaki = NaZakupy("ziemniaki", 20, "kg", 3.26)

ziemniaki.wyswietl_produkt( )
print("\n")
ziemniaki.ile_produktu( )
print("\n")
ziemniaki.ile_kosztuje(10)
print("Cena wynosi: {: .2f}zł".format(ziemniaki.ile_kosztuje(10)))
