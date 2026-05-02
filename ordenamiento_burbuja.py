"Ordenamiento burbuja: ordena una lista comparando elementos adyacentes y permutándolos si están en el orden incorrecto, repitiendo este proceso hasta que la lista esté ordenada."

def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1): # O(n) * O(n) = O(n*n) = O(n^2)
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

if __name__ == "__main__":
    lista = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", lista)
    sorted_lista = ordenamiento_burbuja(lista)
    print("Lista ordenada:", sorted_lista)