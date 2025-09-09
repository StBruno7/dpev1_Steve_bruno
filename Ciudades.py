from Estados import Estados

class Ciudades(Estados):
    def __init__(self):
        super().__init__()
        self.codigoCiudad =""
        self.nombreCiudad =""

    def ingresarDatos(self):
        super().ingresarDatos()
        self.codigoCiudad = input("Ingrese código de la ciudad: ")
        self.nombreCiudad = input("Ingrese nombre de la ciudad: ")
        self.Datos[-1].update({
            "codigoCiudad": self.codigoCiudad,
            "nombreCiudad": self.nombreCiudad
        })