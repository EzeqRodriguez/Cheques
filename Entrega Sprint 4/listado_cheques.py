import csv


def buscarPorDni():

    dni = input("Ingrese su dni: ")

    datos = csv.DictReader(open("test.csv"))

    for linea in datos:
        if linea["DNI"] == dni:
            print(linea)
        else:
            print("El dni no se encuentra en nuestra base de datos")
        break


buscarPorDni()
buscarPorDni()
buscarPorDni()


