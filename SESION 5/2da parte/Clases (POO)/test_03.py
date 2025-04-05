"""
    Programación Orientada a Objetos
    Utilización de métodos
"""

class Carro:
    """Atributo"""
    rueda = 4

    """Constructor: Valores que van a tomar por defecto mi clase que se instancia a una variable"""
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    """Métodos: Son las funciones de las clases"""
    def acelerar(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frenar(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad < 0:
            velocidad = 0
        self.velocidad = velocidad


carro_1 = Carro("Azul", 70)

print(carro_1.velocidad)
carro_1.acelerar()
carro_1.acelerar()
carro_1.acelerar()
carro_1.acelerar()


print("La velocidad actual de mi carro 1 es: {}".format(carro_1.velocidad))

carro_1.frenar()
carro_1.frenar()

print("La velocidad de mi carro 1 es: {}".format(carro_1.velocidad))

