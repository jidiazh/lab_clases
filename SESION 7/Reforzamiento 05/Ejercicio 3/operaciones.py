"""
Módulos

3.	Creando un archivo principal (main.py) donde importará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones:

- Una función que genere 30 números enteros aleatorios entre 0 y 100,
y muestre en pantalla esta lista de números aleatorios
- Otra función que ordene los valores de una lista y volver a mostrarla en pantalla
- Otra función que me indicará cuál es el mayor de todos estos números de la lista

"""

import random


def generar_lista():
    lista = [random.randint(0, 100) for _ in range(30)]
    print("Lista generada aleatoriamente:")
    print(lista)
    return lista


def ordenar_lista(lista):
    lista_ordenada = sorted(lista)
    print("Lista ordenada:")
    print(lista_ordenada)
    return lista_ordenada


def mayor_valor(lista):
    mayor = max(lista)
    print("El número mayor de la lista es: {}".format(mayor))
    return mayor

