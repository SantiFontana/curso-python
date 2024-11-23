meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre");



while True: 
    numero = int(input("Ingresa un número (1-12) para ver el mes, o 0 para salir: "))
    
    if numero == 0:
        print("El programa ha terminado")
        break
    elif 1 <= numero <= len(meses):
        print(f"El mes es {meses [numero -1]}")
    else:
        print("Error número fuera de rango. Por favor, intenta de nuevo.")
        


numeros = []

while True:
    numero = int(input("Ingresa un número (0 para terminar): "))
    
    if numero == 0:
        break
    
    numeros.append(numero)

numeros.sort()

print("Números ordenados de menor a mayor:")
print(numeros)



numeros = (2,3,3,5,4,6,6,7,7,9,2,1,1,2);

numero_usuario = int(input("Ingresa un número para verificar cuántas veces se repite: "));

cantidad = numeros.count(numero_usuario);

print(f"El número {numero_usuario} se repite {cantidad} veces en la tupla.")


frutas = {
    "manzana" : 3,
    "naranja" : 2,
    "banana" : 5,
    "uvas" : 1,
}

nombre_fruta = input("Ingresa el nombre una fruta: ").lower();

if nombre_fruta in frutas:
    
    cantidad = int(input("Ingresa la cantidad de frutas que quieres comprar: "))

    precio_unitario = frutas[nombre_fruta]
    precio_final = precio_unitario * cantidad
    
    print(f"El precio final por {cantidad} {nombre_fruta}(s) es: ${precio_final}")
else:
    print("Lo siento, no tenemos esa fruta en el inventario.")
