"""
Decoradores en Python
"""
# Creación interna de la función decoradora


def funcionDecorado(funcionB):
    def funcionC(*args, **kwargs):
        print("1. Antes de ejecutar la función a decorar")
        resultado = funcionB(*args, **kwargs)
        print("2. Después de ejecutar la función a decorar")
        return resultado
    return funcionC


@funcionDecorado
def saludar(nombre, apellido, edad, **kwargs):
    print("Hola {} {}, usted tiene {} años".format(nombre, apellido, edad))
    for key, value in kwargs.items():
        print("{} = {}".format(key, value))


saludar("Julio", "Gutierrez", 29,
        ciudad_1= "Lima", ciudad_2 = "Tacna", ciudad_3="Arequipa")