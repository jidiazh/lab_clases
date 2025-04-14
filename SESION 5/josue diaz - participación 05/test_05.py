"""
    Programación Orientada a Objetos
    Participación

Requerimientos:
    - Crear una Clase Alumno
    - Debe tener un atributo de nacionalidad con el valor "Peruano"
    - Tendrá 3 notas, la nota inicial de c/u será de 0
    - Crear un método que indicará el promedio del alumno
    - Crear un método que indicará si el alumno está aprobado o no de acuerdo a su promedio
    - Las notas serán pasadas por parámetro al momento de instanciar la clase
    - Crear un método para obtener el nombre y distrito de residencia del alumno
    - Instanciar la clase para el caso de 2 alumnos necesariamente
"""
class Alumno:
    nacionalidad = "Peruano"  # Atributo de clase

    def __init__(self, nombre, distrito, nota1=0, nota2=0, nota3=0):
        self.nombre = nombre
        self.distrito = distrito
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def promedio(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3

    def estado(self):
        if self.promedio() >= 11:
            return "Aprobado"
        else:
            return "Desaprobado"

    def datos_personales(self):
        return "{} vive en {}".format(self.nombre, self.distrito)


# Crear dos alumnos
alumno1 = Alumno("Mia", "Lima", 12, 15, 16)
alumno2 = Alumno("Mariano", "Surco", 9, 10, 8)

# Mostrar información del primer alumno
print("Alumno 1")
print(alumno1.datos_personales())
print("Promedio: {:.2f}".format(alumno1.promedio()))
print("Estado: {}".format(alumno1.estado()))
print("Nacionalidad: {}".format(Alumno.nacionalidad))

print("------------------")

# Mostrar información del segundo alumno
print("Alumno 2")
print(alumno2.datos_personales())
print("Promedio: {:.2f}".format(alumno2.promedio()))
print("Estado: {}".format(alumno2.estado()))
print("Nacionalidad: {}".format(Alumno.nacionalidad))

