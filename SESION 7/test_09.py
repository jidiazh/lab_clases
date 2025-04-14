"""
Decoradores en Python

Función decoradora que valida los argumentos
que se pasan a una función antes que se ejecuta
"""
from pandas.core.computation.common import result_type_many


# Creación interna de la función decoradora

def validar_param_positivos(func):
    def funcB(*args):
        print("1. Evaluando parámetros")
        for arg in args:
            if arg < 0:
                print("Por el valor: {}".format(arg))
                print("Todos los parámetros deben ser positivos")

        resultado = func(*args)

        print("2. Se ejecutó la función y su resultado es: {}".format(resultado))
        return resultado
    return funcB

@validar_param_positivos
def multiplica(a, b, c):
    return a * b * c


multiplica(10, 4, 1)
multiplica(2, 6, 8)
multiplica(1, 3, -4)

