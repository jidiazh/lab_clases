"""
Decoradores

6.	Crear una función decoradora que dará los buenos días antes de ejecutar
una función a ser decorada “Buenos días NOMBRE son las HORA horas con MINUTOS minutos”
y luego de ser ejecutada lanzará un mensaje diciendo “Hasta luego que tenga buen día”.

- La función a decorar pedirá el nombre de una persona y retornará el mensaje.

"""
from datetime import datetime


def dar_buenos_dias(func):
    def wrapper():
        nombre = input("Ingrese su nombre: ")
        ahora = datetime.now()
        print("Buenos días {}, son las {} horas con {} minutos".format(
            nombre, ahora.hour, ahora.minute))
        resultado = func(nombre)
        print("Hasta luego, que tenga buen día.")
        return resultado
    return wrapper


@dar_buenos_dias
def saludar(nombre):
    return "Encantado de saludarte, {}.".format(nombre)


print(saludar())

