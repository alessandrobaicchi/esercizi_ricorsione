# In realtà, in questo esercizio il caso terminale non serve.
# Però, l'abbiamo messo per impratichirci ad usare la struttura classica della ricorsione: if/else.

def count_leaf_nodes(input_list):
    # condizione terminale
    if len(input_list) == 0:
        return 0
    # condizione non terminale
    else:
        counter = 0
        for element in input_list:
            # Check if element is a list
            if type(element) == list:
                counter += count_leaf_nodes(element)
                # If it is a list, we count its elements with a recursion
                # Cioè, aggiungo quello che count_leaf_nodes() troverà nella sottolista. E' ricorsione!
            else:
                counter += 1
                # else, we add +1
                # Cioè, se non è una lista è un elemento da contare subito
        return counter


if __name__ == '__main__':
    names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
    print(count_leaf_nodes(names)) # We expect 10