import numpy as np
# Stwórz listę składającą się z wartości a następnie zapisz 
# do innej zmiennej jej kopię przekonwertowaną na typ int64.
a = np.array([1.0, 2.1, 4.6, 8.1])
b = a.astype('int64')
print("Tablica:",a,"Typ elementów:",a.dtype,"\n"
          "Kopia tablicy:",b,"Typ kopi elementów:",b.dtype)

