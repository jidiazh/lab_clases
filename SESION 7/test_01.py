"""Uso de librerías de fecha y tiempo"""

from datetime import datetime, date

str_date = "2/6/2025"

"""
d: día
m: mes
Y: año
"""

conversion = datetime.strptime(str_date, "%d/%m/%Y")
print(conversion)
print(type(conversion))

"""Traer el mes de la fecha con formato en letras: strftime de datetime"""

conversion_mes = datetime.strftime(conversion, "%d %b del %Y")
print(conversion_mes)

"""
b: reemplaza a 'm' para mostrar el mes de manera literal
"""