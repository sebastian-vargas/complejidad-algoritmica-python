
def morral_01(tamaño_morral, pesos, valores, n=None):
    """
    Algoritmo clásico del problema del morral 0/1 (0/1 Knapsack) usando recursividad.

    Dado un morral con capacidad limitada y una lista de objetos con pesos y valores,
    selecciona objetos completos (no fraccionados) para maximizar el valor total.

    Parámetros:
        tamaño_morral (int): Capacidad máxima del morral.
        pesos (list of int): Pesos de los objetos.
        valores (list of int): Valores de los objetos.
        n (int, opcional): Número de objetos a considerar (por defecto, todos).

    Retorna:
        int: Valor total máximo que puede llevar el morral.
    """
    if n is None:
        n = len(pesos)
    # Indentación para visualizar el nivel de recursión
    nivel = len(pesos) - n
    indent = '|  ' * nivel
    # Caso base: sin objetos o sin capacidad
    if n == 0 or tamaño_morral == 0:
        print(f"{indent}Morral(capacidad={tamaño_morral}, objetos={n}): valor=0  <-- caso base")
        return 0
    print(f"{indent}Morral(capacidad={tamaño_morral}, objetos={n}) -> objeto[{n-1}] peso={pesos[n-1]}, valor={valores[n-1]}")
    # Si el peso del objeto actual es mayor que la capacidad, no se puede incluir
    if pesos[n-1] > tamaño_morral:
        print(f"{indent}No cabe el objeto {n-1} (peso {pesos[n-1]}), lo EXCLUYO.")
        print(f"{indent}" + "-"*40)
        return morral_01(tamaño_morral, pesos, valores, n-1)
    else:
        print(f"{indent}Intento INCLUIR el objeto {n-1}...")
        incluir = valores[n-1] + morral_01(tamaño_morral - pesos[n-1], pesos, valores, n-1)
        print(f"{indent}Intento EXCLUIR el objeto {n-1}...")
        excluir = morral_01(tamaño_morral, pesos, valores, n-1)
        mejor = max(incluir, excluir)
        print(f"{indent}>> Mejor valor con capacidad={tamaño_morral}, objetos={n}: {mejor} (incluyendo={incluir}, excluyendo={excluir})")
        print(f"{indent}" + "="*40)
        return mejor
if __name__ == "__main__":
    # Ejemplo de uso del algoritmo del morral fraccionario
    tamaño_morral = 50
    pesos = [10, 20, 30]
    valores = [60, 100, 120]
    print("\n========= Proceso detallado del algoritmo 0/1 Knapsack =========\n")
    resultado = morral_01(tamaño_morral, pesos, valores)
    print("\n===============================================================")
    print(f"Valor total máximo en el morral (0/1): {resultado}")