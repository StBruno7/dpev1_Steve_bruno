from Ciudades import Ciudades

def menu():
    ciudad = Ciudades()

    while True:
        print("Menú de opciones")
        print("1 = ingresar datos")
        print("2 = mostrar datos")
        print("3 = salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ciudad.ingresarDatos()
            print("Datos ingresados con éxito")
        elif opcion == "2":
            ciudad.mostrarDato()
        elif opcion == "3":
            print("Muchas gracias por usar el software")
            break
        else:
            print("Opción invalida, Vuelva a intentarlo")

if __name__ == "__main__":
    menu()