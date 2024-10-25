import random

numero = random.randint(1, 100)
intentos = 5
intentos_realizados = 0

print("Adivina el número entre 1 y 100")

while intentos_realizados < intentos:
    adivinanza = int(input("Ingresa tu número: "))
    intentos_realizados += 1

    if adivinanza == numero:
        print("¡Felicidades! Has adivinado el número.")
        break
    elif adivinanza < numero:
        print("El número es mayor.")
    else:
        print("El número es menor.")

if adivinanza != numero:
    print(f"Lo siento, perdiste. El número era {numero}.")

print(f"Intentos realizados: {intentos_realizados}/{intentos}")
