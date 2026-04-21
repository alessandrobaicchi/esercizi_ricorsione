# Soluzione usando una classe
import copy


class XExpansion:
    def __init__(self):
        self.soluzioni = []         # E' una lista
        self.soluzioni_list = []   # E' una lista

    # ====================================== Uso di una lista per parziale =======================================
    def calcola_list(self, input):
        self.soluzioni_list = []
        # Qui il parziale è una lista
        self._ricorsione_list([], input)

    def _ricorsione_list(self, parziale: list, rimanenti: str):
        # Caso terminale
        if len(rimanenti) == 0:
            #print(parziale)
            self.soluzioni_list.append(copy.deepcopy(parziale))
        # Caso ricorsivo
        else:
            # Prendo il primo carattere di rimanenti e vedere cosa c'è.
            # 	- se è uno 0 o 1 lo metto in parziale, e chiamo la ricorsione sul resto.
            #	- se è una X devo fare un branching: metto 0 e chiamo il metodo su tutto il
            #	  resto e poi metto 1 e chiamo il metodo su tutto il resto.
            if rimanenti[0] == 'X':
                # parziale.append("0")
                # self._ricorsione_list(parziale, rimanenti[1:])
                # parziale.pop()
                # parziale.append("1")
                # self._ricorsione_list(parziale, rimanenti[1:])
                # parziale.pop()
                # Si può sintentizzare come segue, ciclando sui due possibili step (0 o 1)
                for c in ["0", "1"]:
                    parziale.append(c)
                    self._ricorsione_list(parziale, rimanenti[1:])
                    parziale.pop()

            else:
                parziale.append(rimanenti[0])
                self._ricorsione_list(parziale, rimanenti[1:])
                parziale.pop()

    # ======================================= Uso di una stringa per parziale ==================================
    def calcola(self, input):
        self.soluzioni = []
        # Qui il parziale è una stringa
        self._ricorsione("", input)

    # parziale è la soluzione parziale
    # rimanenti sono il resto dei caratteri da esaminare
    # Ho messo _ perché voglio che il metodo NON sia chiamato dall'esterno.
    def _ricorsione(self, parziale: str, rimanenti: str):
        # Caso terminale
        if len(rimanenti) == 0:
            #print(parziale)
            self.soluzioni.append(parziale)
        # Caso ricorsivo
        else:
            # Prendo il primo carattere di rimanenti e vedere cosa c'è.
            # 	- se è uno 0 o 1 lo metto in parziale, e chiamo la ricorsione sul resto.
            #	- se è una X devo fare un branching: metto 0 e chiamo il metodo su tutto il
            #	  resto e poi metto 1 e chiamo il metodo su tutto il resto.
            if rimanenti[0] == 'X':
                self._ricorsione(parziale + "0", rimanenti[1:])
                self._ricorsione(parziale + "1", rimanenti[1:])
            else:
                self._ricorsione(parziale + rimanenti[0], rimanenti[1:])

# ===============================================================================================================
# Soluzione senza usare una classe, ma direttamente un metodo "classico"

def x_expansion2(input):
    soluzioni = []
    # parziale è la soluzione parziale
    # rimanenti sono il resto dei caratteri da esaminare
    # Ho messo _ perché voglio che il metodo NON sia chiamato dall'esterno.
    def ricorsione(parziale: str, rimanenti: str):
        # Caso terminale
        if len(rimanenti) == 0:
            #print(parziale)
            soluzioni.append(parziale)
        # Caso ricorsivo
        else:
            # Prendo il primo carattere di rimanenti e vedere cosa c'è.
            # 	- se è uno 0 o 1 lo metto in parziale, e chiamo la ricorsione sul resto.
            #	- se è una X devo fare un branching: metto 0 e chiamo il metodo su tutto il
            #	  resto e poi metto 1 e chiamo il metodo su tutto il resto.
            if rimanenti[0] == 'X':
                ricorsione(parziale + "0", rimanenti[1:])
                ricorsione(parziale + "1", rimanenti[1:])
            else:
                ricorsione(parziale + rimanenti[0], rimanenti[1:])

    ricorsione("", input)
    return soluzioni




if __name__ == "__main__":
    sequenza = "01X11XX"
    xexp = XExpansion()

    # Metodo con soluzioni parziali rappresentate come stringhe
    xexp.calcola(sequenza)
    print("Soluzione usando la classe con la stringa")
    print(xexp.soluzioni)

    # Metodo con soluzioni parziali rappresentate come liste
    xexp.calcola_list(sequenza)
    print("Soluzione usando la classe con la lista")
    print(xexp.soluzioni_list)

    # print("\n")
    # print("Soluzione senza usare la classe")
    # print(x_expansion2(sequenza))

    """
    NOTA. _ricorsione è definita dentro una classe, quindi:
    •	NON è una funzione libera
    •	NON è accessibile come _ricorsione()
    •	esiste solo come metodo dell’oggetto
    
    Quindi devo scrivere:
    self._ricorsione(...)
    
    oppure, fuori dalla classe:
    xexp._ricorsione(...)

    """