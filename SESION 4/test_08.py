"""
Requisitos
- Dentro de una empresa se va a solicitar pedir nombre y apellido del empleado (input)
- Distrito de residencia (inputs)
- Sueldo y calculo del bono final del año, que será el triple del sueldo mensualmenos el 10% del sueldo
- Todos estos datos van a ingresar en un diccionario
- Asignar a 3 variables usando asignación múltiple los valores del diccionario
- Mostrar por la terminal el mensaje de: "'Nombre' 'apellido', recibirá 'bono' soles de bono de fin de año"
Hora máximo de envío: 8 pm
"""
#Pidiendo los datos que solicita la empresa
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido paterno: ")
distrito = input("Ingrese el distrito de residencia: ")
sueldo = int(input("Ingrese su sueldo mensual: "))

#Bono final
bono_final = (sueldo*3) - (sueldo*0.1)

#Poniendo los datos en un diccionario
empleado = {
    "nombre": nombre,
    "apellido": apellido,
    "distrito": distrito,
    "sueldo": sueldo,
    "bono": bono_final
}

#Asignando nuevas variables a mi lista

nombre_empleado = empleado["nombre"]
apellido_empleado = empleado["apellido"]
distrito_empleado =  empleado["distrito"]
bono_final = empleado["bono"]


print("{} {}, recibirá {:.2f} soles de bono de fin de año.".format(nombre_empleado, apellido_empleado, empleado["bono"]))
