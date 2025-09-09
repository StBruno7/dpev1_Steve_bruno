from Continentes import Continentes

class Paises(Continentes):
    def __init__(self):
        super().__init__()
        self.codigoPais = ""
        self.nombrePais = ""

    def ingresarDatos(self):
        super().ingresarDatos()
        self.codigoPais = input("Ingrese el código del país: ")
        self.nombrePais = input("Ingrese el nombre del país: ")
        self.Datos[-1].update({
            "codigoPais": self.codigoPais,
            "nombrePais": self.nombrePais
        })