
"""- Crear dos lista de personas vacías
- Agregar los datos de nombre, edad y profesión para ambas listas
- Obtener y mostrar la suma de las edad // por índica
- Sumar ambas listas y mostrar el resultado en la terminal
- Mostrar de manera inversa la suma de ambas listas
- Actualizar la nueva lista eliminando las edades de ambas personas
- Mostrar la lista vacía de la segunda persona aplicando el método respectivamente"""
#listas vacias
persona_1 = []
persona_2 = []
#agregamos elementos
persona_1.append("Carlos")
persona_1.append(30)
persona_1.append("Ingeniero")

persona_2.append("María")
persona_2.append(25)
persona_2.append("Doctora")

# suma de las edades usando los índices
suma_edades = persona_1[1] + persona_2[1]
print("La suma de las edades es:", suma_edades)

# Sumamos ambas listas
lista_suma = persona_1 + persona_2
print("Lista unida:", lista_suma)

# lista sumada en orden inverso

lista_suma. reverse ()
print("Lista unida en orden inverso:{}" .format (lista_suma))

# eliminando las edades de ambas personas
lista_suma.pop(1)
lista_suma.pop(3)

print("Lista sin edades:", lista_suma)

# Vaciar la lista de la segunda persona
persona_2.clear()
print("Lista vacía de la segunda persona:", persona_2)
