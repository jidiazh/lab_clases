#from funciones import *      #No se realiza esto porque sobre carga la memoria
from funciones import suma as opera_1, multiplicacion as opera_2

var_1 = int(input("Primer valor: "))
var_2 = int(input("Segundo valor: "))

#sum = suma(var_1, var_2)
sum = opera_1(var_1, var_2)
print(sum)

#mul = multiplicacion(var_1, var_2)
mul = opera_2(var_1, var_2)
print(mul)