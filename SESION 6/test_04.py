"""
Ejercicio de intervención

Requisitos:
- Agregar una exepción donde se va a considerar una lista con 4 valores,
todos sus datos serán string
- Al querer modificar una de las posiciones no existentes
crear un nuevo índice y darle el valor de "0"
- Mostrar la lista final
"""

mi_lista = ["uno", "dos", "tres", "cuatro"]

print("Lista original:", mi_lista)

indice_str = input("¿Qué índice querés modificar? ")
valor_nuevo = input("¿Qué valor querés poner? ")

try:
    indice = int(indice_str)
    mi_lista[indice] = valor_nuevo
except IndexError:
    print("El índice {} no existe. Se agregará ese índice con valor '0'.".format(indice))
    while len(mi_lista) <= indice:
        mi_lista.append("0")

print("Lista final:", mi_lista)
