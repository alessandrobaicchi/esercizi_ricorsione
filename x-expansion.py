class XExpansion:
    def __init__(self):
        soluzioni = []

    def calcola(self, input):
        self._ricorsione("", input)

    # parziale è la soluzione parziale
    # rimanenti sono il resto dei caratteri da esaminare
    # Ho messo _ perché voglio che il metodo NON sia chiamato dall'esterno.
    def _ricorsione(self, parziale: str, rimanenti: str):
        # Caso terminale
        if len(rimanenti) == 0:
            print(parziale)
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

if __name__ == "__main__":
    sequenza = "01X0X"
    xexp = XExpansion()
    #xexp.calcola(sequenza)
    xexp._ricorsione("", sequenza)


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