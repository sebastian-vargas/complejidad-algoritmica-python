def ordenamiento_por_insercion(lista):

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual
        
if __name__ == "__main__":
    lista = [12, 11, 13, 5, 6]
    print("Lista original:", lista)
    ordenamiento_por_insercion(lista)
    print("Lista ordenada:", lista)