#creando una lista con list
lista = list([20,65,88,True])

#devuelve la cantidad de elementos
cantidad_elementos = len(lista)

#agregando un elemento a la lista
lista.append(12)

#agregando un elemento en un indice especifico
lista.insert(2,"MATE")

#agregando varios elementos a la lista
lista.extend([False,2024])

#eliminando un elemento de la lista (por su indice)
lista.pop(3) #-1 para eliminar el ultimo elemento, -2 para el anteultimo y asi sucesivamente

#removiendo un elemento de la lista por su valor
lista.remove("MATE")

#eliminando todos los elementos de la lista
#lista.clear()

#ordenando la lista de forma ascendente (si usamos el parametro reverse=True lo ordena en reversa)
lista.sort()

#invirtiendo los elementos de una lista sin ordenarla
lista.reverse()

#verificando si un elemento esta en la lista
elemento_encontrado = lista.index(65)

print(elemento_encontrado)