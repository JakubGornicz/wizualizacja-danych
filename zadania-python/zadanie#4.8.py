class Robaczek :
    def __init__ (self, x, y) :
        self.x = x
        self.y = y
        self.krok = 10
    def idz_w_gore(self, ile_krokow) :
        self.y = self.y + ile_krokow * self.krok
    def idz_w_dol(self, ile_krokow) :
        self.y = self.y - ile_krokow * self.krok
    def idz_w_lewo(self, ile_krokow) :
        self.x = self.x - ile_krokow * self.krok
    def idz_w_prawo(self, ile_krokow) :
        self.x = self.x + ile_krokow * self.krok

    def pokaz_gdzie_jestes(self) :
        print("x={}, y={}".format(self.x, self.y))

    def __del__(self) :
        print("Wywolano finalizer, usunięto robaka")

robal = Robaczek(100, 100)
robal.idz_w_gore(3)
robal.idz_w_dol(1)
robal.idz_w_lewo(3)
robal.idz_w_prawo(1)
robal.pokaz_gdzie_jestes( )

del robal
