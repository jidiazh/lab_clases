"""if ternarios"""

"""
Requisitos: 
 - Ingresar por teclado el sueldo de un empleado
 - Si el sueldo es mayor a 2500 y menor a 3500, imprimir "Su sueldo no tiene bonificación"
 y se le agregará el 10%, para luego mostrar el sueldo final con la bonificación
 - Caso contrario: "Su sueldo tiene bonificación este año y será de: 
 'sueldo_final'", sueldo_final= sueldo + 2% sueldo
"""
sueldo = float(input("Ingresar el sueldo del trabajador: "))

# uso del operador ternario de if para el saldo final
sueldo_final = sueldo * 1.10 if 2500 < sueldo < 3500 else sueldo * 1.02

if 2500 < sueldo < 3500:
    print("Su sueldo no tiene bonificación")  # pero se le agregará un 10%.
    print("El sueldo final con bonificación es: {:.2f}".format(sueldo_final))
else:
    print("Su sueldo tiene bonificación este año y será de: {:.2f}".format(sueldo_final))

