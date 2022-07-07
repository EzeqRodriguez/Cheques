import csv

with open('test.csv', 'r') as datos:

    cheques = csv.DictReader(datos)
    
    dni = input("Para ver sus cheques, Ingrese su dni: ")
    
    for cheque in cheques:

        if dni == cheque["DNI"]:
            print(f"Sus cheques: \n{cheque}")

        

