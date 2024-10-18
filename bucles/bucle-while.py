#creando un contador que va a ir sumandose
contador = 0

# mientras que la condicion se cumpla, el bucle se va seguir ejecutando
# (vuelta, tras vuelta se verifica la condicion)
while contador < 16:
    contador += 1

print(contador)
    

# otro ejemplo pidiendo numeros al usuario
contador = 1
suma = 0

corte = int(input("¿Cuantos numeros queres agregar? "))

while contador <= corte:
    nota = float(input("Ingrese nota: "))
    suma += nota
    contador += 1

print(suma)


# otro ejemplo con break
password = "holiwis"
incorrecta = True
intentos = 1
nombre = input("Ingresa tu nombre: ")

while incorrecta:
    password2 = input("ingrese contraseña:")
    if password == password2:
        break
    intentos += 1
    
print(f"Hola {nombre}, ingresaste al sistema luego de {intentos} intentos")