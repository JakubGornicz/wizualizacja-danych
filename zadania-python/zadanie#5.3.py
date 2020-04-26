class Ksztalty:
    # definicja konstruktora
    def __init__(self, x, y):
        # deklarujemy atrybuty
        # self wskazuje że chodzi o zmienne właśnie definiowanej klasy
        self.x=x 
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik
        
class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x = x
        self.y = x

    def __ge__(self, other): #a, b a >= b
             return self.x >= other.x  
    def __gt__(self, other): #a, b a > b
            return self.x > other.x
    def __lt__(self, other): #a, b a < b
            return  self.x < other.x
    def __le__(self, other): #a, b a <= b
            return self.x <= other.x  

kw1 = Kwadrat(5)
kw2 = Kwadrat(7)

print("Czy wiekszy/rowny: ",kw1>=kw2)

print("Czy wiekszy: ",kw1>kw2)

print("Czy mniejszy: ",kw1<kw2)

print("Czy mniejszy/rowny: ",kw1<=kw2)



