import matplotlib.pyplot as plt
import numpy as np

zawodnicy = ['debil1', 'debil2', 'debil3', 'debil4']
bramki = [48, 19, 22, 10]

wedges, texts, autotexts = plt.pie(bramki, labels=zawodnicy, autopct=lambda pct: '{:.1f}%'.format(pct), textprops=dict(color='black'))
plt.setp(autotexts, size=10, weight='bold')
plt.title('pierwsza wersja wykresu')
plt.legend(title='Zawodnicy', loc='upper left')
plt.show()
