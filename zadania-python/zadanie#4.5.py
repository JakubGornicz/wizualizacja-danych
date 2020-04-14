class ciag_arytmetyczny:

    global ciag

    def Update(self):
        self.ciag = [self.pierwsza_wart]
        for i in range(self.ile_elementow - 1):
            self.ciag.append(self.pierwsza_wart + self.roznica)
            self.pierwsza_wart += self.roznica

    def __init__(self, pierwsza_wart, roznica, ile_elementow):
        self.pierwsza_wart = pierwsza_wart
        self.roznica = roznica
        self.ile_elementow = ile_elementow
        self.Update()

    def wyswietl_dane(self):
        print(*self.ciag, sep=", ", end="\n")

    def pobierz_elementy(self):
        for i in range(self.ile_elementow):
            self.ciag[i] = int(input("Podaj element: "))

    def pobierz_parametry(self):
        self.pierwsza_wart = int(input("Podaj nowy pierwszy wyraz: "))
        self.roznica = int(input("Podaj nową różnicę: "))
        self.ile_elementow = int(input("Podaj nową liczbę elementów: "))
        self.Update()

    def policz_sume(self):
        sum = 0
        for i in range(self.ile_elementow):
            sum += self.ciag[i]
        print("Suma ciagu wynosi: ", sum)

    def policz_elementy(self):
        sum = 0
        for i in range(self.ile_elementow):
            sum = sum + 1
        print("Suma elementow: ", sum)


pewien_ciag = ciag_arytmetyczny(1, 1, 10)

pewien_ciag.wyswietl_dane( )

pewien_ciag.pobierz_elementy( )
pewien_ciag.wyswietl_dane( )

pewien_ciag.pobierz_parametry( )
pewien_ciag.wyswietl_dane( )

pewien_ciag.policz_sume( )

pewien_ciag.policz_elementy( )
