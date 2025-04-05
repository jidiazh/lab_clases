"""Uso del método random"""

import random

numero = random.randint(1, 100)
print(numero)

mi_lista = []

for elemento in range(10):
    #le concedemos un valor aleatorio entre el 1 y 30
    elemento = random.randint(1, 30)
    #agregamos el número aleatorio a la lista vacía
    mi_lista.append(elemento)

print("Mi lista actualizada tiene los siguiente valores: {}".format(mi_lista))