import time


class NRegine():    # Perché ()? In Python 3 è indifferente mettere o no in una classe le ().
                    # Le () servivano in Python 2 per specificare l'ereditarietà.

    def __init__(self):
        self.n_soluzioni = 0
        self.n_chiamate = 0

    # ====================================== APPROCCIO 2 =================================================
    def solve2(self, N):
        self.n_soluzioni = 0    # Conta quante soluzioni sono state trovate
        self.n_chiamate = 0     # Conta il numero di chiamate alla funzione ricorsiva
        # Rappresento questo parziale come una lista
        self._ricorsione2([], N)


    # parziale è un vettore di coppie (riga, colonna)
    def _ricorsione2(self, parziale, N):
        self.n_chiamate += 1
        # Caso terminale: ho messo N regine
        if len(parziale) == N:
            # if self._is_soluzione(parziale):
            #     self.n_soluzioni += 1
            #     print(parziale)
            # Con _step_is_valid() verifico passo passo l'ammissibilità di una nuova regina (nuova_regina),
            # e quindi è superfluo verificare di nuovo tutto alla fine con _is_soluzione().
            self.n_soluzioni += 1
            print(parziale)
        # Caso ricorsivo: ho messo un numero di regine < N
        else:
            for riga in range(N):       # Col doppio for sto andando a verificare tutte le possibili celle
                for col in range(N):
                    # Verifico che la nuova_regina sia ammissibile
                    nuova_regina = [riga, col]
                    if self._step_is_valid(nuova_regina, parziale):
                        # Aggiungo un pezzetto di soluzione in parziale
                        parziale.append(nuova_regina)    # Appendo una nuova regina
                        # Vado avanti con la ricorsione
                        self._ricorsione2(parziale, N)
                        # Backtracking
                        parziale.pop()


    # Funzione che controlla se la nuova_regina che voglio inserire sia ammissibile rispetto
    # alla soluzione parziale costruita sinora
    def _step_is_valid(self, nuova_regina, parziale) -> bool:
        for regina in parziale:
            if not self._is_pair_admissible(nuova_regina, regina):
                return False
        return True


    # Funzione che prende due regine alla volta e restituisce True se possono stare insieme sulla scacchiera
    # Altrimenti, restituisce False
    def _is_pair_admissible(self, regina1, regina2) -> bool:
        # regina1 è quella che già ho, regina2 è quella che voglio testare, ogni regina è una lista

        # 1) Verifico la riga, se non va bene return False
        if regina1[0] == regina2[0]:
            return False

        # 2) Verifico la colonna, se non va bene return False
        if regina1[1] == regina2[1]:
            return False

        # 3) Verifico la diagonale 1, se non va bene return False
        # La diagonale maggiore si identifica in questo modo. Sono tutti gli elementi della
        # scacchiera tali che: indice colonna - indice riga = costante, nello specifico:
        # colonna di regina1 - riga di regina1 == colonna di regina2 - riga di regina2
        if regina1[1] - regina1[0] == regina2[1] - regina2[0]:
            return False

        # 4) Verifico la diagonale 2, se non va bene return False
        # La diagonale minore si identifica in questo modo. Sono tutti gli elementi della
        # scacchiera tali che: indice colonna + indice riga = costante, nello specifico:
        # colonna di regina1 + riga di regina1 == colonna di regina2 + riga di regina2
        if regina1[1] + regina1[0] == regina2[1] + regina2[0]:
            return False

        # 5) Se passa tutti i controlli, return True
        return True


    # Metodo che, data una possibile soluzione (lista con N regine), verifica se sia una soluzione ammissibile.
    # Se ammissibile restituisce True, se non ammissibile restituisce False
    def _is_soluzione(self, soluzione_possibile) -> bool:
        for i in range(len(soluzione_possibile) - 1):
            for j in range( i+1, len(soluzione_possibile)):
                if not self._is_pair_admissible(soluzione_possibile[i], soluzione_possibile[j]):
                    # Se la coppia di regine confrontate non è ammissibile -> False
                    return False
        # Se invece tutte le possibili coppie di regine sono ammissibili -> True
        return True
    # NOTA. Il metodo _step_is_valid() verifica passo passo l'ammissibilità di una nuova regina (nuova_regina),
    # e quindi è superfluo verificare di nuovo tutto alla fine con _is_soluzione().

    # ====================================================================================================

if __name__ == '__main__':
    nreg = NRegine()
    start_time = time.time()
    nreg.solve2(4)
    end_time = time.time()

    print(f"Tempo di elaborazione: {end_time - start_time}")
    print(f"Ho trovato {nreg.n_soluzioni} soluzioni possibili")
    print(f"Chiamate effettuate: {nreg.n_chiamate}")