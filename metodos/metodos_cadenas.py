cadena1 = "hola,soy,santiago"
cadena2 = "Bienvenido Maquinola"

#CONVIERTE A MAYUSCULAS
mayusc = cadena1.upper()

#convierte a minusculas
minusc = cadena1.lower()

#Primera letra En Mayuscula y el resto en minuscula
primer_letra_mayusc = cadena1.capitalize()

#Buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1
busqueda_find = cadena1.find("z")

#Buscamos una cadena en otra cadena, si no hay coincidencias lanza una excepción
busqueda_index = cadena1.index("a")

#si es numerico, deuelve True, sino devuelve False
es_numerico = cadena1.isnumeric()

#si es alfanumérico, deuelve True, sino devuelve False
es_alfanumerico = cadena1.isalpha()

#contamos coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("soy")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
empieza_con = cadena1.startswith("h")

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
termina_con = cadena1.endswith("ago")

#si el valor 1 se encuentra en la cadena original, reemplaza el valor 1 de la misma por el valor 2
cadena_nueva = cadena1.replace(","," ")

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")

print(cadena_separada)