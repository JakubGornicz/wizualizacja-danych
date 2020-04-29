def fib( ):
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

a = fib( )
#aby pokazać jak działa generator, wypisujemy np. pierwsze 50 wyrazów
#ale ponieważ jest on oparty na pętli "while True" możemy policzyć watość
#dowolnego elementu tego ciągu
for i in range(50): 
    print(next(a))
        
