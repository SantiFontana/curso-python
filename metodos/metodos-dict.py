diccionario = {
    "nombre" : "Santiago",
    "apellido" : "Fontana",
    "edad" : "20"
}

#agrega un elemento al diccionario
diccionario["pais"] = "Argentina"

#devuelve las claves (también nos sirve para iterar)
claves = diccionario.keys()

#devuelve el valor de una clave
claves = diccionario.get("edad")

#eliminando todo el diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("apellido")

#obteniendo un elemento dict_items() iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)