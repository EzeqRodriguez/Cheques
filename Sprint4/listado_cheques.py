import csv

def menu():

    opcion=int(input("Bienvenido: \nIngrese 1, para ver todos sus cheques\nIngrese 2, para ver sus cheques APROBADOS\nIngrese 3, para ver sus cheques RECHAZADOS\n"))

    if opcion==1:
        verCheques()
    elif opcion==2:
        verAprobado()
    elif opcion==3:
        verRechazado()
    else:
        print("Opcion incorrecta, intente nuevamente")

def verCheques():

    with open('Sprint4/test.csv', 'r') as dato:

        cheques = csv.DictReader(dato)

        dni=input("Ingrese su  DNI para ver todos sus cheques:\n")

        for cheque in cheques:

            if dni==cheque["DNI"]:
                print("Nro de Cheque: ",cheque["NroCheque"])
                print("Codigo del Banco: ",cheque["CodigoBanco"])
                print("Codigo de la Sucursal: ",cheque["CodigoSucursal"])
                print("CBU de Origen: ",cheque["NumeroCuentaOrigen"])
                print("CBU de Destinatario: ",cheque["NumeroCuentaDestino"])
                print("Valor del Cheque: ",cheque["Valor"])
                print("Fecha de Origen del Cheque: ",cheque["FechaOrigen"])
                print("Fecha de  Pago del Cheque: ",cheque["FechaPago"])
                print("Tipo de Cheque: ",cheque["Tipo"])
                print("Estado del Cheque: ",cheque["Estado"])
                print("\n")
        # return(dato)

def verAprobado():

    with open('Sprint4/test.csv', 'r') as dato:

        cheques = csv.DictReader(dato)

        dni=input("Ingrese su DNI para ver sus cheques Aprobados:\n")
        
        for cheque in cheques:
        
            if dni==cheque["DNI"] and cheque["Estado"]=="APROBADO":
                print("Nro de Cheque: ",cheque["NroCheque"])
                print("Codigo del Banco: ",cheque["CodigoBanco"])
                print("Codigo de la Sucursal: ",cheque["CodigoSucursal"])
                print("CBU de Origen: ",cheque["NumeroCuentaOrigen"])
                print("CBU de Destinatario: ",cheque["NumeroCuentaDestino"])
                print("Valor del Cheque: ",cheque["Valor"])
                print("Fecha de Origen del Cheque: ",cheque["FechaOrigen"])
                print("Fecha de  Pago del Cheque: ",cheque["FechaPago"])
                print("Tipo de Cheque: ",cheque["Tipo"])
                print("Estado del Cheque: ",cheque["Estado"])
                print("\n")
            # return(dato)
        
def verRechazado():

    with open('Sprint4/test.csv', 'r') as dato:

        cheques = csv.DictReader(dato)

        dni=input("Ingrese su DNI para ver sus cheques Rechazados:\n")
        
        for cheque in cheques:
        
            if dni==cheque["DNI"] and cheque["Estado"]=="RECHAZADO":
                print("Nro de Cheque: ",cheque["NroCheque"])
                print("Codigo del Banco: ",cheque["CodigoBanco"])
                print("Codigo de la Sucursal: ",cheque["CodigoSucursal"])
                print("CBU de Origen: ",cheque["NumeroCuentaOrigen"])
                print("CBU de Destinatario: ",cheque["NumeroCuentaDestino"])
                print("Valor del Cheque: ",cheque["Valor"])
                print("Fecha de Origen del Cheque: ",cheque["FechaOrigen"])
                print("Fecha de  Pago del Cheque: ",cheque["FechaPago"])
                print("Tipo de Cheque: ",cheque["Tipo"])
                print("Estado del Cheque: ",cheque["Estado"])
                print("\n")
            # return(dato)


continuaMenu = "1"
while continuaMenu=="1":
    menu()
    continuaMenu=input("Para volver, presione 1\npara salir, presione cualquier tecla\n")
    if continuaMenu != "1":
        print("Gracias, por elegirnos")
