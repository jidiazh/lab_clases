"""
Decoradores en Python
"""
# Creación interna de la función decoradora

def funcionDecoradora(funcionB):

    def funcionC():
        print("1. Antes de ejecutar la función a decorar")
        funcionB()
        print("2. Después de ejecutar la función a decorar")

    return funcionC()

@funcionDecoradora
def saludo():
    print("Hola Pythonistas")

#saludo()
