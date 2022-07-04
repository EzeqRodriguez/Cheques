import csv
def buscarPorDni():



    with open("test.csv", newline='') as f:
        reader = csv.DictReader(f)
        dni = input("Ingrese su dni: ")
        for linea in reader:
            if dni == linea["DNI"]:
                print(linea)
            #else:
                #print("Su DNI no esta en nuestra base de datos; Intente nuevamente.")  

buscarPorDni()  
buscarPorDni()
buscarPorDni()      
        

