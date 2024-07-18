import random


trabajadores = ["Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez", "Pedro Rodriguez",
                "Laura Hernandez", "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]


def asignar_sueldos():
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]
    return sueldos

def clasificar_sueldos(sueldos):
    rango_bajo = []
    rango_medio = []
    rango_alto = []
    
    for i, sueldo in enumerate(sueldos):
        if sueldo < 800000:
            rango_bajo.append((trabajadores[i], sueldo))
        elif 800000 <= sueldo <= 2000000:
            rango_medio.append((trabajadores[i], sueldo))
        else:
            rango_alto.append((trabajadores[i], sueldo))
    

def mostrar_menu():
    print("________Menú:________")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadisticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")


    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            sueldos = asignar_sueldos()
            print("Sueldos aleatorios asignados correctamente.")

        elif opcion == '2':
            if not sueldos:
                print("Primero debe asignar sueldos aleatorios.")
            else:
                clasificar_sueldos(sueldos)
