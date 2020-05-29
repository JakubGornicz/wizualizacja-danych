import numpy as np
# Wykorzystaj poznane na zajęciach funkcje biblioteki Numpy i stwórz
# macierz 5x5, która będzie zawierała kolejne wartości ciągu Fibonacciego.
def fib(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

n = 5 
mat = np.arange(1, n*n+1)
for i in range(0,n*n) :
    mat[i] = fib(i)
mat = mat.reshape((n,n))

print(mat)
