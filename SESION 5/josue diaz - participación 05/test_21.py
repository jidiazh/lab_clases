"""
Programación funcional con Python (POO)

Requisitos:
    - Solicitar al usuario 4 números por consola
    - Crear una función que devuelva cuál es el número mayor de los 4
      ingresados por el usuario
    - Finalmente asignar a una variable el valor de esta función
      para elevar al cubo este resultado y mostrarlo en la terminal
"""

a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))
d = int(input("Ingresa el cuarto número: "))

def numero_mayor(a,b,c,d):
    if a > b and a > c and a > d:
        return (a)
    elif b > a and b > c and b > d:
        return (b)
    elif c > a and c > b and c > d:
        return (c)
    else:
        return (d)

mayor = numero_mayor(a, b, c, d)

cubo_mayor = pow(mayor, 3)


print("El número mayor es: {}".format(mayor))
print("El cubo del número mayor es: {}".format(cubo_mayor))
