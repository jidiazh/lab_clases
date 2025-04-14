"""
Módulos

2. Creando un archivo principal (main.py) donde importará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones:
- Una función que realizará la carga de un valor entero y que verifique
que solamente tiene que ser numérico
- Una función que mostrará por pantalla la raíz cuadrada de dicho valor
- Y otra función el valor elevado al cuadrado y al cubo de dicho número,
puedes devolver un diccionario
- Utilizar el módulo math de python

"""

import math


def cargar_valor():
    while True:
        try:
            valor = int(input("Ingrese un número entero: "))
            return valor
        except ValueError:
            print("Error: Solo se permiten números enteros.")


def raiz_cuadrada(numero):
    raiz = math.sqrt(numero)
    print("La raíz cuadrada de {} es {:.2f}".format(numero, raiz))
    return raiz


def potencias(numero):
    resultado = {
        "cuadrado": math.pow(numero, 2),
        "cubo": math.pow(numero, 3)
    }
    print("El número {} al cuadrado es {} y al cubo es {}".format(
        numero, int(resultado["cuadrado"]), int(resultado["cubo"])))
    return resultado

