def merge_sort(arr, nivel=0):
    """
    Ordena una lista usando el algoritmo de mezcla (merge sort).

    Parámetros:
        arr (list): Lista de elementos a ordenar.

    Retorna:
        list: Nueva lista ordenada.

    El algoritmo divide la lista en mitades, ordena cada mitad recursivamente y luego las mezcla.
    Complejidad temporal: O(n log n)
    """
    indent = '  ' * nivel
    print(f"{indent}Dividiendo: {arr}")
    if len(arr) <= 1:
        print(f"{indent}Retornando: {arr}")
        return arr

    # Encontrar el punto medio y dividir la lista
    mid = len(arr) // 2
    left  = merge_sort(arr[:mid], nivel + 1)
    right = merge_sort(arr[mid:], nivel + 1)

    # Mezclar las dos mitades ordenadas
    mezclada = merge(left, right)
    print(f"{indent}Mezclando: {left} + {right} -> {mezclada}")
    return mezclada


def merge(left, right):
    """
    Mezcla dos listas ordenadas en una sola lista ordenada.

    Parámetros:
        left (list): Primera lista ordenada.
        right (list): Segunda lista ordenada.

    Retorna:
        list: Nueva lista ordenada combinando ambas.
    """
    result = []  # Lista resultado
    i = j = 0    # Punteros para recorrer left y right

    # Comparar elementos de ambas listas y agregar el menor
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Agregar los elementos restantes de left (si hay)
    result.extend(left[i:])
    # Agregar los elementos restantes de right (si hay)
    result.extend(right[j:])
    return result

# Ejemplo de uso
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Lista original:", arr)
    print("\nProceso de ordenamiento:")
    resultado = merge_sort(arr)
    print("\nLista ordenada:", resultado)  # [3, 9, 10, 27, 38, 43, 82]