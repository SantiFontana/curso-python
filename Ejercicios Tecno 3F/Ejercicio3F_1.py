import random

numero = random.randint(1, 100)
intentos = 7
intentos_realizados = 0

print("Adivina el número entre 1 y 100")

while intentos_realizados < intentos:
    adivinanza = input("Ingresa tu número: ")
    if adivinanza.isdigit():
        adivinanza = int(adivinanza)
        intentos_realizados += 1
        if adivinanza > 1 and adivinanza < 100:
            if adivinanza == numero:
                print("¡Felicidades! Has adivinado el número.")
                break
            elif adivinanza < numero:
                print("El número es mayor.")
            else:
                print("El número es menor.")
        else:
            print("El numero esta fuera del rango")
    else:
        print("Solo se aceptan numeros enteros")
if adivinanza != numero:
    print(f"Lo siento, perdiste. El número era {numero}.")

print(f"Intentos realizados: {intentos_realizados}/{intentos}")
