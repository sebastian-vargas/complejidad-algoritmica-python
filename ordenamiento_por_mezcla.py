def ordenamiento_por_mezcla(lista, nivel=0):
	"""
	Ordena una lista usando el algoritmo de mezcla (merge sort).
	Divide la lista en mitades, ordena cada mitad y luego las mezcla.
	Complejidad: O(n log n)
	"""
	indent = '  ' * nivel
	if len(lista) > 1:
		medio = len(lista) // 2
		izquierda = lista[:medio]
		derecha = lista[medio:]

		print(f"{indent}{izquierda}")
		print(f"{indent}{derecha}")

		ordenamiento_por_mezcla(izquierda, nivel + 1)
		ordenamiento_por_mezcla(derecha, nivel + 1)

		i = 0
		j = 0
		k = 0

		while i < len(izquierda) and j < len(derecha):
			if izquierda[i] < derecha[j]:
				lista[k] = izquierda[i]
				i += 1
			else:
				lista[k] = derecha[j]
				j += 1
			k += 1

		while i < len(izquierda):
			lista[k] = izquierda[i]
			i += 1
			k += 1

		while j < len(derecha):
			lista[k] = derecha[j]
			j += 1
			k += 1

		print(f"{indent}{lista}")


if __name__ == "__main__":
	lista = [38, 27, 43, 3, 9, 82, 10]
	print("Lista original:", lista)
	ordenamiento_por_mezcla(lista)
	print("Lista ordenada:", lista)
