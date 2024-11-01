
while True:
    try:
        numero = int(input("Ingresa un número: "))

        if numero > 0:
            print("Programa Iniciado")

            frase = input("Dime una palabra o frase: ")
            cantidad_caracteres = len(frase)
            print(f"La cantidad de caracteres es: {cantidad_caracteres}");

            factorial = 1
            for i in range(1, cantidad_caracteres + 1):
                factorial *= i
            print(f"El factorial de {cantidad_caracteres} es: {factorial}")

            
            if factorial % 2 == 0:
                    print("El factorial es par")
            else:
                    print("El factorial es impar")
        else: 
            print("Programa finalizado")
            break
        

    except ValueError:
        print("No has ingresado un número válido. Programa finalizado.")
    break
