from functools import lru_cache
#from time import time
from time import perf_counter

class Fibonacci:
    def __init__(self):
        self.cache = {0: 0, 1: 1}   # E' un dizionario che contiene (memorizza) le soluzioni già calcolate
        self.ricorsioni = 0     # Serve per contare quante volte viene fatta la ricorsione
        self.ricorsioni_cache = 0

    def calcola_elemento_cache(self, n):
        # Se ho già la soluzione per questo n, allora la prendo dalla cache
        if self.cache.get(n) is not None:
            # Se il valore di .get() non è None, significa che la soluzione già c'è,
            # e quindi la restituisco.
            return self.cache[n]
        # Altrimenti devo calcolarla con la ricorsione
        else:
            self.ricorsioni_cache += 1
            self.cache[n] = (self.calcola_elemento_cache(n-1)
             + self.calcola_elemento_cache(n-2))
            return self.cache[n]


    def calcola_elemento(self,n):
        # condizione terminale
        if n ==0 :
            return 0
        elif n==1 :
            return 1
        # condizione non terminale (ricorsivo)
        else:
            self.ricorsioni += 1
            return (self.calcola_elemento(n-1) +
                    self.calcola_elemento(n-2))


    @lru_cache(maxsize=None)
    def calcola_elemento_lru(self,n):
        # caso terminale
        if n ==0 :
            return 0
        elif n==1 :
            return 1
        # caso ricorsivo
        else:
            return (self.calcola_elemento_lru(n-1) +
                    self.calcola_elemento_lru(n-2))

if __name__ == '__main__':
    N = 40
    fib = Fibonacci()

    #start_time = time()
    start_time = perf_counter()
    print(fib.calcola_elemento(N))
    #end_time = time()
    end_time = perf_counter()
    print(f"Elapsed time - recursion: {end_time - start_time:.6f} seconds")
    print(fib.ricorsioni)

    #start_time = time()
    start_time = perf_counter()
    print(fib.calcola_elemento_cache(N))
    #end_time = time()
    end_time = perf_counter()
    print(f"Elapsed time - cache: {end_time - start_time:.6f} seconds")
    print(fib.ricorsioni_cache)

    # start_time = time()
    # print(fib.calcola_elemento_lru(N))
    # end_time = time()
    # print(f"Elapsed time - lru: {end_time - start_time}")