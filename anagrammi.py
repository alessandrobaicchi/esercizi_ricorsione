import copy
from functools import lru_cache

# ============================================================
# VERSIONE 1 — parziale come LISTA (MUTABILE) + soluzioni LISTA
#
# ⚠️ ATTENZIONE: la lista è MUTABILE → tutte le chiamate ricorsive
# condividono lo *stesso oggetto* 'parziale'.
#
# CONSEGUENZE:
# - append() modifica la lista originale
# - pop() è OBBLIGATORIO per fare backtracking
# - quando salvo la soluzione, NON posso fare append(parziale)
#   perché salverei un riferimento allo stesso oggetto
#   → tutte le soluzioni si sovrascrivono tra loro
#
# SOLUZIONE:
# ✔ usare copy.deepcopy(parziale) nel caso terminale
# ✔ usare parziale.pop() dopo la ricorsione
#
# IDEA CHIAVE:
# La ricorsione lavora sempre sulla *stessa lista*.
# Senza deepcopy + pop, le soluzioni finali sono sbagliate.
# ============================================================


def anagrammi(parola):
    soluzioni = []
    ricorsione([], parola, soluzioni)
    return soluzioni


def ricorsione(parziale: list, rimanenti: str, soluzioni: list) -> list:
    # Caso terminale
    if len(rimanenti) == 0:
        soluzioni.append(copy.deepcopy(parziale))
    # Caso ricorsivo
    else:
        for i in range(len(rimanenti)):                         # Es. DOG
            parziale.append(rimanenti[i])                       # parziale = D
            nuovi_rimanenti = rimanenti[:i] + rimanenti[i+1:]   # nuovi_rimanenti = OG
            ricorsione(parziale, nuovi_rimanenti, soluzioni)    # ricorsione( D, OG, soluzioni)
            parziale.pop()                                      # parziale = ''



# ============================================================
# VERSIONE 2 — parziale come STRINGA (IMMUTABILE) + soluzioni SET
#
# ✔ La stringa è IMMUTABILE → ogni concatenazione crea un NUOVO oggetto.
#   Questo elimina completamente i problemi della mutabilità.
#
# VANTAGGI:
# - NON serve pop() → non c’è backtracking manuale
# - NON serve deepcopy() → ogni stringa è già una copia autonoma
# - posso usare un SET perché la stringa è hashable
#   → elimina automaticamente le permutazioni duplicate
#
# IDEA CHIAVE:
# Ogni chiamata ricorsiva riceve una stringa nuova.
# Nessuna chiamata modifica lo stato delle altre.
# È la versione più elegante e sicura.
# ============================================================

def anagrammi_str(parola):
    soluzioni = set()
    ricorsione_str("", parola, soluzioni)
    return soluzioni


def ricorsione_str(parziale: str, rimanenti: str, soluzioni: set) -> set:
    # Caso terminale
    if len(rimanenti) == 0:
        #soluzioni.add(copy.deepcopy(parziale))
        soluzioni.add(parziale)
    # Caso ricorsivo
    else:
        for i in range(len(rimanenti)):
            nuovi_rimanenti = rimanenti[:i] + rimanenti[i+1:]
            ricorsione_str(parziale + rimanenti[i], nuovi_rimanenti, soluzioni)




# ============================================================
# VERSIONE 3 — parziale STRINGA + LRU CACHE + stampa diretta
#
# ✔ La stringa è IMMUTABILE → perfetta per la cache (hashable).
# ✔ La cache evita di ricalcolare combinazioni già viste.
#
# ⚠️ MA ATTENZIONE:
# La funzione NON restituisce un valore → fa SOLO print().
# La cache memorizza l'output della prima chiamata e
# NON riesegue più la funzione per input già visti.
#
# RISULTATO:
# - le stampe successive NON vengono eseguite
# - la cache “uccide” gli effetti collaterali (qui print)
#
# IDEA CHIAVE:
# La cache funziona SOLO con funzioni PURE (senza effetti collaterali).
# Se la funzione stampa, la cache elimina le stampe duplicate.
# ============================================================

def anagrammi_str2(parola):
    ricorsione_str2("", parola)

@lru_cache(maxsize=None)        # parziale e rimanenti sono due stringhe, quindi input hashable: ok!
def ricorsione_str2(parziale: str, rimanenti: str):
    # Caso terminale
    if len(rimanenti) == 0:
        print(parziale)
    # Caso ricorsivo
    else:
        for i in range(len(rimanenti)):
            nuovi_rimanenti = rimanenti[:i] + rimanenti[i+1:]
            ricorsione_str2(parziale + rimanenti[i], nuovi_rimanenti)



# ================================================ TEST =====================================================

if __name__ == "__main__":
    print(anagrammi('casa'))

    print(anagrammi_str("casaaaa"))

    anagrammi_str2("aaaa")