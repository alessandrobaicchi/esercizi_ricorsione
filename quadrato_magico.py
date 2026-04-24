from time import time


class QuadratoMagico:
    def __init__(self, N):
        self.N = N
        self.n_chiamate = 0
        self.n_soluzioni = 0


    # Soluzione del quadrato magico, rappresentata da un vettore di N^2 elementi. Ogni elemento
    # rappresenta una cella del quadrato magico e il suo valore è il numero che mettiamo nella cella.
    def risolvi_quadrato(self):
        self.n_soluzioni = 0
        self.n_chiamate = 0
        self._ricorsione([])


    def _ricorsione(self, parziale):
        self.n_chiamate += 1
        # Caso terminale
        if len(parziale) == self.N*self.N:      # len(parziale) == N^2
            self.n_soluzioni += 1
            print(parziale)
        # Caso ricorsivo
        else:
            for numero in range(1, self.N*self.N+1):
                # 1) Aggiungere numero a parziale (che è una lista)
                parziale.append(numero)
                # 2) Andare avanti nella ricorsione
                self._ricorsione(parziale)
                # 3) Fare backtracking
                parziale.pop()


if __name__ == '__main__':
    qm = QuadratoMagico(2)
    start_time = time()
    qm.risolvi_quadrato()
    end_time = time()
    print(f"Tempo impiegato: {end_time - start_time}")
    print(f"Chiamate effettuate: {qm.n_chiamate}")
    print(f"Soluzione trovate: {qm.n_soluzioni}")
