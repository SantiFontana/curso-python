
#le pedimos al usuario que diga una frase (o varias)
frase = input("Decime algo, y te calculo cuanto tardarías si tuvieras que decirla: ")

#creamos una lista con todas las palabras de la frase (se separan cada vez que haya un espacio en blanco)
palabras_separadas = frase.split(" ")

#usamos len() para ver la cantidad de elementos que hay en la lista
cantidad_de_palabras = len(palabras_separadas)

#en caso de que tarde más de un minuto en decirlo, le decimos que pare un poco
if cantidad_de_palabras > 120:
    print("Para, tampoco te pedi un testamento")

#Calculamos cuanto tardaría en decir las palabras y se lo decimos
print(f"Dijiste {cantidad_de_palabras}, y tardarías {cantidad_de_palabras/2} segundos en decirlo")
print(f"Dalto tardaría {round(cantidad_de_palabras * 100 // 2 * 1.3 / 100,2)} segundos en decirlo")