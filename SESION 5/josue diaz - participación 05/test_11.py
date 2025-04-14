"""Usando las propiedades de cadenas o string"""

"""
Requisitos:
 - Ingresar tu nombre y apellido por consola 
 (cada valor tiene que estar en una variable distinta)
 - Obtener el tamaño de tu nombre y apeellido completo luego de concatenarlos
 y mostrar en consola
 - Imprimir el resultado de la concatenación final todo en mayúsculas
 - Indicar mediante condicionales si el tamaño del nombre es mayor 
 o no al del apellido ingresado
 (Ingresar solo en este caso el apellido paterno)
 """
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido paterno: ")

nombre_completo = nombre +" "+ apellido
longitud_total = len(nombre_completo)

print("Tamaño del nombre completo: {} caracteres".format(longitud_total))
print("Nombre completo en mayúsculas: {}".format(nombre_completo.upper()))

# Comparaciòn de las longitudes
if len(nombre) > len(apellido):
    print("El nombre es más largo que el apellido")
else:
    print("El nombre no es más largo que el apellido")