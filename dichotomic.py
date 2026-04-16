def dichotomic(input_list, val):
    # Caso terminale
    # Se la lista ha un solo elemento -> confronto diretto:
    #   - se è uguale a val -> True
    #   - altrimenti -> False
    if len(input_list) == 1:
        if input_list[0] == val:
            return True
        else:
            return False
    # Caso ricorsivo
    # Divido la lista in due metà:
    # - richiamo la funzione su entrambe
    # - se almeno una metà contiene val -> True
    else:
        index = len(input_list)//2      # Es: 5 // 2 = 2,5 -> 2
        return (dichotomic(input_list[:index], val) or dichotomic(input_list[index:], val))

if __name__ == "__main__":
    sequenza = [1,2,3,4,5,6,7,8,9]
    print(dichotomic(sequenza,4))   # True
    print(dichotomic(sequenza,11))  # False

