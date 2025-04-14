"""
Decoradores

7.	Haciendo el uso de *args y **kwargs aplicarlo debidamente para decorar decorar
una función que recibirá 6 argumentos los cuales se multiplicarán entre ellos
(3 de ellos serán usados con **kwargs)

Mensaje previo al usar el decorador “Está por ejecutarse la función”
y mensaje luego de usar el decorador “La función ha sido ejecutado correctamente”

"""

def decorador_mensaje(func):
    def wrapper(*args, **kwargs):
        print("Está por ejecutarse la función")
        resultado = func(*args, **kwargs)
        print("La función ha sido ejecutado correctamente")
        return resultado
    return wrapper


@decorador_mensaje
def multiplicar_valores(*args, **kwargs):
    resultado = 1

    for valor in args:
        resultado *= valor

    for valor in kwargs.values():
        resultado *= valor

    print("Resultado de la multiplicación:", resultado)
    return resultado


multiplicar_valores(2, 3, 4, x=5, y=2, z=1)

