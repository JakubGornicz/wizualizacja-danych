tab_miesiace = ["styczeń", "luty", "marzec","kwiecień","maj","czerwiec","lipiec",
                            "sierpień","wrzesień","październik","listopad","grudzień"]
def month( ):
    i=0
    while True:
        if(i>11):
            i = 0
        yield tab_miesiace[i]
        i = i + 1
        
m = month( )
for j in range(len(tab_miesiace)):
    print(next(m))
#Ponieważ po grudniu następuje styczeń, a nie koniec świata, generator się
#zapętla.
print(next(m))
print(next(m))
print(next(m))
#...
