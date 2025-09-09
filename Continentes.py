class Continentes:
    def __init__(self):
        self.codigoContinente=""
        self.nombreContinente=""
        self.Datos = []

    def ingresarDatos(self):
        self.codigoContinente = input("Ingrese código del continente: ")
        self.nombreContinente = input("Ingrese nombre del continente: ")
        self.Datos.append({
            "codigoContinente" : self.codigoContinente,
            "nombreContinent" : self.nombreContinente
        })

    def mostrarDato(self):
        if not self.Datos:
            print("No existen datos aun")
            return

        for i, Dato in enumerate(self.Datos, start=1):
            print(f"Registro número {i}")
            for clave, valor in Dato.items():
                print(f"{clave}: {valor}")