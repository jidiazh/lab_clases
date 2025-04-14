"""Uso de la librería JON para tratar tipo de datos JSON"""

import json

data_python = {'nombre': "Milagros", 'edad': 32, 'distrito': 'Jesús María'}

"""Convirtiendo a un dato tipo JSON: dumps()"""

date_python_to_json = json.dumps(data_python)

print(date_python_to_json)
print(type(date_python_to_json))
