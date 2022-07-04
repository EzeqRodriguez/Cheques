import csv

def buscarPorDni():
    
    with open("test.csv") as archivo:
        
        lineas = csv.DictReader(archivo)
        
        dni = input("Ingrese su dni: ")
        
        for linea in lineas:
            
            if dni == linea["DNI"]:
                print(linea)
            #else:
                #print("Su DNI no esta en nuestra base de datos; Intente nuevamente.")       
            
buscarPorDni()
buscarPorDni()
buscarPorDni()
        

