import pandas as pd

from zadanie_8_01 import *

# Z danych z zadania 1 wyświetl
# (korzystając w miarę możliwości z funkcji biblioteki Pandas):

print("\nPODPUNKT 1\n")
# - tylko te rekordy gdzie liczba nadanych imion
# była większa niż 1000 w danym roku
over1000_df = df.loc[ df['Liczba'] > 1000]
print(over1000_df.head(3))
print(over1000_df.tail(3))

print("\nPODPUNKT 2\n")
#- tylko rekordy gdzie nadane imię jest takie jak Twoje
my_name_df = df.loc[ df['Imię'] == "JAKUB"]
print(my_name_df)

print("\nPODPUNKT 3\n")
#- sumę wszystkich urodzonych dzieci w całym danym okresie
suma_dzieci_df = df.groupby('Rok').sum( )
print(suma_dzieci_df)

print("\nPODPUNKT 4\n")
# - sumę dzieci urodzonych w latach 2000-2005
ile = df.loc[ df['Rok'] <= 2005 ]
ile = ile['Liczba'].sum( )
print("W przedziale od 2000 do 2005 urodziło się:",ile)

print("\nPODPUNKT 5\n")
# - sumę urodzonych chłopców i dziewczynek
total = suma_dzieci_df['Liczba'].sum( )
print("Łącznie od 2000 do 2019 urodziło się:", total)

print("\nPODPUNKT 5\n")
# - najbardziej popularne imię dziewczynki i chłopca
# w danym roku ( czyli po 2 rekordy na rok),

