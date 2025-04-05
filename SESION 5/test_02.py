"""Uso del condicional if"""

edad = int(input("Ingrese su edad por favor: "))

if 0 < edad < 18:
    print("Usted todavía es menor de edad")
elif 18 <= edad < 65:
    print("Usted es una persona adulta")
elif 65 <= edad < 100:
    print("Usted es un adulta de la tercera edad")
else:
    print("Usted ha ingresado una edad incorrecta, ingrese una edad válida por favor")