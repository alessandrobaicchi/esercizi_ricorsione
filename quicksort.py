
def quicksort(sequenza):
    # Caso terminale
    if len(sequenza) <= 1:
        return sequenza
    # Caso ricorsivo
    else:
        # 1. Prendo un elemento a caso come pivot, ad esempio il primo di sequenza
        pivot = sequenza[0]
        # 2. Divido sequenza secondo il pivot
        # sequenza_smaller = []
        # sequenza_pivot = []
        # sequenza_larger = []
        # for i in sequenza:
        #     # Il numero i è minore del pivot
        #     if i < pivot:
        #         sequenza_smaller.append(i)
        #     # Il numero i è uguale al pivot
        #     elif i == pivot:
        #         sequenza_pivot.append(i)
        #     # Il numero i è maggiore del pivot
        #     else:
        #         sequenza_larger.append(i)
        # Soluzione più compatta di tutto il blocco 2
        sequenza_smaller = [n for n in sequenza if n < pivot]
        sequenza_pivot = [n for n in sequenza if n == pivot]
        sequenza_larger = [n for n in sequenza if n > pivot]

        # 3. La soluzione è data da: ordinare il vettore smaller + il vettore uguale al pivot +
        #                            ordinare il vettore larger
        return (quicksort(sequenza_smaller)+sequenza_pivot+quicksort(sequenza_larger))

if __name__ == "__main__":
    sequenza = [9, 3, 2, 6, 8, 5, 199]
    print(quicksort(sequenza))