animales = ["gato", "perro", "loro", "cocodrilo"]
numeros = [52,16,14,72]

#recorriendo la lista animales
for animal in animales:
    print(f"Ahora la variable animal es igual a: {animal}")
    
#recorriendo la lista numeros y multiplicando cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)

#iterando dos listas del mismo tamaño al mismo tiempo
for numero,animal in zip(animales,numeros):
    print(f"Recorriendo lista 1: {numero}")
    print(f"Recorriendo lista 2: {animal}")

#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"El índice es: {indice} y el valor es: {valor}")

#usando el for/else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("El bucle terminó")
    
#todo lo anterior funciona exactamente igual para tuplas y conjuntos