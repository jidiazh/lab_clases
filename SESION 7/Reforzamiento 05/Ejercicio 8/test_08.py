"""
Decoradores

8.	Crear un decorador donde imprimirá la cantidad de argumentos que tiene
la función a decorar usando *args y **kwargs.
Mensaje previo “La cantidad de argumentos que tiene la función es {}”
mensaje post “La función decoradora terminó de ejecutarse correctamente”

Ejemplo: Al usar una función suma que creamos y usamos
suma(4, 1, 10, 2, 50, 64)
El decorador determinará la cantidad de argumentos que tiene la función al decorarla.

Salida:
“La cantidad de argumentos que tiene la función es”
5
“La función decoradora terminó de ejecutarse correctamente”

"""

def decorador_argumentos(func):
    def wrapper(*args, **kwargs):
        total = len(args) + len(kwargs)
        print("La cantidad de argumentos que tiene la función es {}".format(total))
        resultado = func(*args, **kwargs)
        print("La función decoradora terminó de ejecutarse correctamente")
        return resultado
    return wrapper


@decorador_argumentos
def suma(*args, **kwargs):
    total = sum(args) + sum(kwargs.values())
    print("El resultado de la suma es:", total)
    return total


# Ejemplo de ejecución
suma(4, 1, 10, 2, 50, 64)

