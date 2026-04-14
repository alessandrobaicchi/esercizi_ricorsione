from time import sleep

# REGOLA.
# Tipicamente, più codice scrivo e più c'è la possibilità che faccio errori.
# Il mio obiettivo è scrivere meno codice possibile e che sia il più semplice possibile.
# In questo esercizio sul countdown non conviene usare la ricorsione!


# Soluzione iterativa
def countdown(n):
    while n >= 0:
        print(n)
        sleep(1)    # sleep() fa una pausa in secondi (qui 1 s) in stile countdown
        n -= 1

# Soluzione ricorsiva
def countdown_recursive(n):
    #condizione terminale
    if n == 0:
        print("Stop")
    #condizione non terminale
    else:
        print(n)
        sleep(1)
        countdown_recursive(n-1)

if __name__ == '__main__':
    N = 4
    countdown_recursive(N)
