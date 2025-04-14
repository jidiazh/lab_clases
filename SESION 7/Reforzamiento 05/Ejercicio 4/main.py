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

from operaciones import cargar_tres_numeros, sumar_dos_valores

# Cargar 3 números
numeros = cargar_tres_numeros()

# Sumar los dos primeros valores
sumar_dos_valores(numeros[0], numeros[1])

