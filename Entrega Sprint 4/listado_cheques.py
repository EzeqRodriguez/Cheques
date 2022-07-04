import csv

def buscarPorDni():
    
    dni=input("Ingrese su dni: ")
    
    datos = csv.reader(open("test.csv"))
    
    for linea in datos:
        if dni == linea[8]:
            print(f'\n El valor del cheque es de: {linea[5]} - Su numero de cheque es: {linea[0]} - El estado es: {linea[9]} - El codigo de sucursal es: {linea[2]}')
        else:
            print("Error su dni no esta en nuestra base de datos, intente nuevamente")       
        

buscarPorDni()



