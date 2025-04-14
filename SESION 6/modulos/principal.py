"""
Ejercicio de intervención

Requisitos:
1. Crear un módulo donde se va a tener que crear una función que obtiene
el impuesto que va a pagar una persona si el sueldo es mayor a 500 soles,
impuesto: 8%

2. Esta función usará una exception si el sueldo es tipo string

3. Pedir el sueldo por consola en el archivo principal

4. El archivo principal importará a la función creada para ser usada

"""
from impuesto import calcular_impuesto

sueldo_input = input("Ingrese su sueldo en soles: ")

try:
    impuesto = calcular_impuesto(sueldo_input)
    if impuesto > 0:
        print("El impuesto a pagar es: {:.2f} soles".format(impuesto))
    else:
        print("No tiene que pagar impuesto, ya que el sueldo es menor o igual a 500 soles.")
except ValueError as e:
    print("Error: {}".format(e))
