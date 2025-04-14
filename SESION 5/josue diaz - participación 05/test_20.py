"""
Programación funcional con Python (POO)

Requisitos:
    - Crear una función que multiplicará 3 valores y luego restará el segundo parámetro
    - Para esta función el tercer parámetro contendrá un valor
    - Mostrar 2 casos donde se ingrese los valores donde uno no afectará
    el valor del parámetro que ya contiene un valor
    y otro donde si lo estará afectando
"""

def multiplicar_y_restar(a, b, c=7):
    resultado = a * b * c - b
    return resultado

# Caso 1: Usando el valor por defecto de c
resultado1 = multiplicar_y_restar(3, 4)  # c toma el valor por defecto = 2
print("Caso 1 (c no modificado):", resultado1)

# Caso 2: Afectando el valor de c
resultado2 = multiplicar_y_restar(3, 4, 9)  # c ahora vale 5
print("Caso 2 (c modificado):", resultado2)
