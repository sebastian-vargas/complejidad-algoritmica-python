def ordenamiento_por_mezcla(lista):
	"""
	Ordena una lista usando el algoritmo de mezcla (merge sort).
	Divide la lista en mitades, ordena cada mitad y luego las mezcla.
	Complejidad: O(n log n)
	"""
	if len(lista) > 1:
		# 1. Encontrar el punto medio y dividir la lista
		medio = len(lista) // 2
		izquierda = lista[:medio]
		derecha = lista[medio:]

		# 2. Ordenar recursivamente cada mitad
		ordenamiento_por_mezcla(izquierda)
		ordenamiento_por_mezcla(derecha)

		# 3. Mezclar las mitades ordenadas
		i = 0  # índice para izquierda
		j = 0  # índice para derecha
		k = 0  # índice para lista principal

		while i < len(izquierda) and j < len(derecha):
			if izquierda[i] < derecha[j]:
				lista[k] = izquierda[i]
				i += 1
			else:
				lista[k] = derecha[j]
				j += 1
			k += 1

		# Copiar los elementos restantes (si hay)
		while i < len(izquierda):
			lista[k] = izquierda[i]
			i += 1
			k += 1

		while j < len(derecha):
			lista[k] = derecha[j]
			j += 1
			k += 1


if __name__ == "__main__":
	lista = [38, 27, 43, 3, 9, 82, 10]
	print("Lista original:", lista)
	ordenamiento_por_mezcla(lista)
	print("Lista ordenada:", lista)
