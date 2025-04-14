"""
Módulos

4. Creando un archivo principal donde llamará a un módulo (operaciones.py)
el cuál contendrá las siguientes funciones:

-La primera función cargará a 3 números enteros que pedirá al usuario
que ingrese por consola un valor.
-La segunda función solamente sumará dos valores.
-Desde el archivo principal importar al módulo y sumar dos valores
usando las funciones anteriormente creadas en el módulo.
"""

def cargar_tres_numeros():
    numeros = []
    for i in range(1, 4):
        while True:
            try:
                valor = int(input("Ingrese el número {}: ".format(i)))
                numeros.append(valor)
                break
            except ValueError:
                print("Error: debe ingresar un número entero.")
    return numeros


def sumar_dos_valores(a, b):
    resultado = a + b
    print("La suma de {} y {} es: {}".format(a, b, resultado))
    return resultado
