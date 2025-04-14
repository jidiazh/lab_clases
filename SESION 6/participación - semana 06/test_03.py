"""Control o gestión de excepciones"""

"""
Requisitos:
    - Crear una función aplicando exceptions donde el bloque except
    va a considerar a los errors de división entre cero y el tipo de error
    - Los valores tienen que ser mayor a 0
    - Los valores tienen que ser ingresado por consola
"""
def dividir():
    try:
        num1 = float(input("Ingresá el primer número (mayor a 0): "))
        num2 = float(input("Ingresá el segundo número (mayor a 0): "))

        if num1 <= 0 or num2 <= 0:
            raise ValueError("Los números deben ser mayores a 0")

        resultado = num1 / num2
        print("El resultado de dividir {} entre {} es: {:.2f}".format(num1, num2, resultado))

    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    except ValueError as ve:
        print("Error de valor: {}".format(ve))
    except TypeError:
        print("Error de tipo: Asegurate de ingresar solo números.")
    except Exception as e:
        print("Error inesperado: {}".format(e))

dividir()
