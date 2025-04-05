"""Diccionarios en python"""

"""del : elimina un key y su valor del diccionario"""

var_1 = {"nombre": "Mathius", "edad": 20, "promedio": 14.5}

var_1["distrito"] = "La Victoria"
del var_1["edad"]
del var_1["promedio"]

print(var_1)