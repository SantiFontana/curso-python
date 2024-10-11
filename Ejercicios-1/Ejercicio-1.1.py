# Promedio de duración
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

# Duración de crudos
crudo_promedio = 5
crudo_dalto = 3.5

# Diferencia de duración
diferencia_con_min = round(100 - dalto_curso / otros_cursos_min * 100, 2)
diferencia_con_max = round(100 - dalto_curso * 100 / otros_cursos_max, 2)
diferencia_con_promedio = round(100 - dalto_curso / otros_cursos_promedio * 100, 2)

# Calculando el porcentaje de tiempo vacío removido
tiempo_vacio_promedio = round(100 - otros_cursos_promedio * 100 / crudo_promedio, 2)
tiempo_vacio_dalto = round(100 - dalto_curso * 100 / crudo_dalto, 2)

# Mostrando las diferencias de duración (Ejercicio A)
print("------------------")
print("El curso de Dalto dura:")
print(f" - un {diferencia_con_min}% menos que el más rápido")
print(f" - un {diferencia_con_max}% menos que el más lento")
print(f" - un {diferencia_con_promedio}% menos que el promedio")
print("------------------")

# Mostrando la cantidad de espacios vacíos que se remueven (Ejercicio B)
print(f"Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacío")
print(f"Este curso promedio eliminó el {tiempo_vacio_dalto}% de tiempo vacío")
print("------------------")

# Mostrando diferencias si los cursos duraran 10 horas
equivalencia_otros_cursos = round(otros_cursos_promedio * 10 / dalto_curso, 2)
equivalencia_dalto_curso = round(dalto_curso * 10 / otros_cursos_promedio, 2)
print(f"10 horas de este curso equivale a ver {equivalencia_otros_cursos} horas de otros cursos")
print(f"10 horas de otros cursos equivale a ver {equivalencia_dalto_curso} horas de este curso")
print("------------------")
