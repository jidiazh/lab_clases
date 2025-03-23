"""
Requisitos
1.Crear 2 variables enteros.2 variables flotantes, 1 variable string (solamente caracteres), 1 variable string con contenido solamente numerico
 y 1 variable boolean
2. Obtener y mostrar la suma de un variable entera con la variable string numerica (realizar conversion si es necesario)
3. Obtener y mostrar la suma de 2 variables enteras mas la variable string numerica y la variable flotante
4. Obtener y mostrar el modulo de las variables enteras:%
5. Obtener y mostrar el resultado o la parte entera de las 2 variables int: //
6. Obtener una pontencia usando una de las variables flotantes como base y la variable entera como potencia

"""
print("----------------")
"""creando variables"""
var_int_1 = 200
var_int_2 = 140
var_float_1 = 20.35
var_float_2 = 12.69
var_str_1 = "Bienvenidos"
var_str_2 = "350"
var_boo = True


suma_1 = var_int_1+ int(var_str_2)
print("Suma de entero_1 con variable string numérica:", suma_1)

suma_2 = var_int_1 + var_int_2 + int(var_str_2) + var_float_1
print("Suma de 2 enteros, string numérica y flotante:", suma_2)

modulo = var_int_1 % var_int_2
print("Módulo de las variables enteras:", modulo)

# 5. Parte entera de la división entre las variables enteras
division_entera = var_int_1 //  var_int_2
print("Parte entera de la división:", division_entera)

potencia = var_float_1 ** var_int_2
print("Potencia de flotante elevado a entero:", potencia)












