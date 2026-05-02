"Llamadas recursivas => crecimiento exponencial. mas de una llamada recurdiva dentro de la función."
def fibonacci(n):
    # Recursividad múltiple
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
# O(2**n)
# Bloque para ejecutar la función de la ley de la multiplicación


"Un loop dentro de otro => crecimiento cuadratico - polimonial."
def f_mult(n):
    # Ley de la multiplicación
    for i in range(n):
        for j in range(n):
            print(i, j)
# O(n) * O(n) = O(n * n) = O(n^2)


"Un loop => crecimiento lineal."
def f_sum_2(n):
    # Ley de la suma
    for i in range(n):
        print(i)

    for i in range(n * n):
        print(i)
# O(n) + O(n * n) = O(n + n^2) = O(n^2)

"Un loop => crecimiento lineal."
def f_sum_1(n):
    for i in range(n):
        print(i)

    for i in range(n):
        print(i)
# O(n) + O(n) = O(n + n) = O(2n) = O(n)

if __name__ == "__main__":
    print("Ejemplo de ley de la fibonacci con n=12:")
    print(fibonacci(12))