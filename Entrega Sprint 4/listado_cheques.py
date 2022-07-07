import csv

with open('Entrega Sprint 4/test.csv', 'r') as datos:

    cheques = csv.DictReader(datos)
    
    dni = input("Para ver sus cheques, Ingrese su dni: ")
    print("Sus cheques: \n")
    for cheque in cheques:

        if dni == cheque["DNI"]:
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
            print("\n\n")
        

