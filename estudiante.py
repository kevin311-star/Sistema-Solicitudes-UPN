
# Clase para guardar los datos del estudiante

class Estudiante:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def mostrar_datos(self):
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
