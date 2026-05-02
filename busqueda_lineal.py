#Busqueda lineal: busca un elemento en una lista recorriendo cada uno de los elementos hasta encontrarlo o llegar al final de la lista.
import random


def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

if __name__ == "__main__":
    tamaño_de_lista = int(input("Ingrese el tamaño de la lista: "))
    objetivo = int(input("Ingrese el número a buscar: "))
    
    lista = [random.randint(0, 100) for _ in range(tamaño_de_lista)]
    
    print("Lista generada:", lista)
    print(f'El elemento {objetivo} {"está" if busqueda_lineal(lista, objetivo) != -1 else "no está"} en el índice: {busqueda_lineal(lista, objetivo)}')
    #print(f"Índice del número buscado: {busqueda_lineal(lista, objetivo)}")