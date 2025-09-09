from Paises import Paises

class Estados(Paises):
    def __init__(self):
        super().__init__()
        self.codigoEstado = ""
        self.nombreEstado = ""
        self.descripcion = ""

    def ingresarDatos(self):
        super().ingresarDatos()
        self.codigoEstado = input("Ingrese código del estado: ")
        self.nombreEstado = input("Ingrese nombre del estado: ")
        self.descripcion = input("Ingrese descripción del estado: ")
        self.Datos[-1].update({
            "nombreEstad": self.codigoEstado,
            "nombrepais": self.nombreEstado,
            "descripcio": self.descripcion
        })