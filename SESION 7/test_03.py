"""
Uso de librerías de fecha y tiempo
Conversión total del tiempo
"""

from datetime import datetime

"""uso del método timestamp"""

time_now = datetime.strptime("2025/05/02 20:30:00",
                             "%Y/%m/%d %H:%M:%S").timestamp()
"""
H: Hora
m: Minuto
S: Segundo
"""
print(time_now)