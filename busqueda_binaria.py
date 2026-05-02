#Busqueda binaroia: busca un elemento en una lista ordenada dividiendo repetidamente el rango de búsqueda a la mitad hasta encontrar el elemento o determinar que no está presente.import random
import random


def busqueda_binaria(lista, comienzo, final, objetivo,iter_bin=0):
    """
    Realiza una búsqueda binaria recursiva en una lista ordenada para encontrar un elemento.

    Args:
        lista (list): Lista ordenada donde buscar.
        comienzo (int): Índice inicial del rango de búsqueda.
        final (int): Índice final del rango de búsqueda.
        objetivo (int): Elemento a buscar.
        iter_bin (int): Contador de iteraciones (para seguimiento).

    Returns:
        tuple: (True/False si se encontró el elemento, número de iteraciones)

    Ejemplo:
        >>> lista = [1, 3, 5, 7, 9]
        >>> busqueda_binaria(lista, 0, len(lista)-1, 5)
        (True, 2)
        >>> busqueda_binaria(lista, 0, len(lista)-1, 4)
        (False, 3)
    """
    iter_bin+=1
    if comienzo > final:
        return (False,iter_bin)

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return (True,iter_bin)
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo,iter_bin=iter_bin)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo,iter_bin=iter_bin)


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamaño es la lista? '))
    objetivo = int(input('¿Qué número quieres encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])

    (encontrado,iter_bin) = busqueda_binaria(lista, 0, len(lista), objetivo)

    #print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(f'Iteraciones busqueda binaria: {iter_bin}')