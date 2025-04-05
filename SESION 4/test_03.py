"""Diccionarios en Python"""

"""del: elimina un key y su valor del diccionario"""

var_1 = {"nombre": "Susana", "edad": 29, "promedio": 18}

var_1["distrito"] = "Lince"
del var_1["edad"]
del var_1["promedio"]

print(var_1)
"""Diccionarios en Python"""

"""sorted: obtener los valores de los key de un diccionario"""

var_1 = {"nombre": "MYSQL", "tipo": "BD relacional"}

keys = sorted(var_1)

print(var_1)
print(keys)