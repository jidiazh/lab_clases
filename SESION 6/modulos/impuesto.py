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


def calcular_impuesto(sueldo):
    try:
        sueldo = float(sueldo)

        if sueldo > 500:
            impuesto = sueldo * 0.08  # 8% de impuesto
            return impuesto
        else:
            return 0

    except ValueError:
        raise ValueError("El sueldo debe ser un número válido.")
