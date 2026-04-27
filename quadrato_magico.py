import copy
from time import time


class QuadratoMagico:
    def __init__(self, N):
        self.N = N
        self.n_chiamate = 0
        self.n_soluzioni = 0
        self.soluzioni = []


    # Soluzione del quadrato magico, rappresentata da un vettore di N^2 elementi. Ogni elemento
    # rappresenta una cella del quadrato magico e il suo valore è il numero che mettiamo nella cella.
    def risolvi_quadrato(self):
        self.n_soluzioni = 0
        self.n_chiamate = 0
        self.soluzioni = []
        self._ricorsione([],set(range(1, self.N*self.N+1))) # Il set contiene rimanenti


    def _ricorsione(self, parziale, rimanenti):
        self.n_chiamate += 1
        # Caso terminale
        if len(parziale) == self.N*self.N:      # len(parziale) == N^2
            if self._is_valid(parziale):        # Facendo il controllo parziale questo controllo è inutile
                self.n_soluzioni += 1
                self.soluzioni.append(copy.deepcopy(parziale))
                #print(parziale)
        # Caso ricorsivo
        else:
            for numero in rimanenti:
                # 1) Aggiungere numero a parziale (che è una lista)
                parziale.append(numero)
                if self._is_parziale_valid(parziale):
                    # 1bis) Tolgo il numero appena inserito da rimanenti
                    nuovi_rimanenti = copy.deepcopy(rimanenti)
                    nuovi_rimanenti.remove(numero)
                    # nuovi_rimanenti sarà il numero rimanenti che serve SOLO alla funzione interna
                    # in 2)nessun altro lo usa, e quindi non ci saranno problemi di più funzioni
                    # che tentano di modificare la stessa cosa.
                    # 2) Andare avanti nella ricorsione
                    self._ricorsione(parziale, nuovi_rimanenti)
                # 3) Fare backtracking
                parziale.pop()


    def _is_parziale_valid(self, parziale):
        numero_magico = self.N*(self.N*self.N+1)/2
        # 1) Controllo righe
        n_righe_completate = len(parziale)//self.N
        for id_riga in range(n_righe_completate):
            riga = parziale[id_riga*self.N:(id_riga+1)*self.N]
            if sum(riga) != numero_magico:
                return False
        # 2) Controllo colonne
        n_col_completate = max(len(parziale) - self.N*(self.N-1),0)
        for id_col in range(n_col_completate):
            col = parziale[id_col: (self.N-1)*self.N + id_col+1: self.N]
            if sum(col) != numero_magico:
                return False
        # # 3) Controllo diagonale 1 (maggiore)
        # diagonale1 = potenziale_soluzione[0 : self.N*self.N+1 : self.N+1]
        # if sum(diagonale1) != numero_magico:
        #     return False
        # # 4) Controllo diagonale 2 (minore)
        # somma = 0
        # for indice in range(self.N):
        #     somma += potenziale_soluzione[indice*self.N + (self.N-1 - indice)]
        # if somma != numero_magico:
        #     return False
        # # 5) Se tutti i controlli sono passati, return True
        return True

    # _is_parziale_valid() rende inutile questo metodo
    def _is_valid(self, potenziale_soluzione):
        numero_magico = self.N*(self.N*self.N+1)/2
        # 1) Controllo righe
        for id_riga in range(self.N):
            riga = potenziale_soluzione[id_riga*self.N:(id_riga+1)*self.N]
            if sum(riga) != numero_magico:
                return False
        # 2) Controllo colonne
        for id_col in range(self.N):
            col = potenziale_soluzione[id_col: (self.N-1)*self.N + id_col+1: self.N]
            if sum(col) != numero_magico:
                return False
        # 3) Controllo diagonale 1 (maggiore)
        diagonale1 = potenziale_soluzione[0 : self.N*self.N+1 : self.N+1]
        if sum(diagonale1) != numero_magico:
            return False
        # 4) Controllo diagonale 2 (minore)
        somma = 0
        for indice in range(self.N):
            somma += potenziale_soluzione[indice*self.N + (self.N-1 - indice)]
        if somma != numero_magico:
            return False
        # 5) Se tutti i controlli sono passati, return True
        return True



    def stampa_quadrato(self, soluzioni):
        print("----------------------------")
        for riga in range(self.N):
            print(soluzioni[riga*self.N:(riga+1)*self.N])
        print("----------------------------")




if __name__ == '__main__':
    qm = QuadratoMagico(3)
    start_time = time()
    qm.risolvi_quadrato()
    end_time = time()
    print(f"Tempo impiegato: {end_time - start_time}")
    print(f"Chiamate effettuate: {qm.n_chiamate}")
    print(f"Soluzione trovate: {qm.n_soluzioni}")
    for soluzione in qm.soluzioni:
        qm.stampa_quadrato(soluzione)
