import random
from statistics import mean, geometric_mean
import csv


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
    
    print("Sueldos menores a $800.000")
    print("TOTAL:", len(rango_bajo))
    print("Nombre empleado\tSueldo")
    for nombre, sueldo in rango_bajo:
        print(f"{nombre}\t${sueldo}")
    
    print("\nSueldos entre $800.000 y $2.000.000")
    print("TOTAL:", len(rango_medio))
    print("Nombre empleado\tSueldo")
    for nombre, sueldo in rango_medio:
        print(f"{nombre}\t${sueldo}")
    
    print("\nSueldos superiores a $2.000.000")
    print("TOTAL:", len(rango_alto))
    print("Nombre empleado\tSueldo")
    for nombre, sueldo in rango_alto:
        print(f"{nombre}\t${sueldo}")
    
    print("TOTAL SUELDOS: $", sum(sueldos))
def calcular_estadisticas(sueldos):
    sueldo_maximo = max(sueldos)
    sueldo_minimo = min(sueldos)
    sueldo_promedio = mean(sueldos)
    sueldo_media_geom = geometric_mean(sueldos)
    return sueldo_maximo, sueldo_minimo, sueldo_promedio, sueldo_media_geom

def generar_reporte(sueldos):
    with open('reporte_sueldos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nombre empleado', 'Sueldo Base', 'Descuento Salud', 'Descuento AFP', 'Sueldo Liquido'])
        for i, sueldo in enumerate(sueldos):
            desc_salud = sueldo * 0.07
            desc_afp = sueldo * 0.12
            sueldo_liquido = sueldo - desc_salud - desc_afp
            writer.writerow([trabajadores[i], sueldo, desc_salud, desc_afp, sueldo_liquido])
    print("Archivo 'reporte_sueldos.csv' generado correctamente.")


def mostrar_menu():
    print("________Menú:________")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadisticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")

def main():
    sueldos = []
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


        elif opcion == '3':
            if not sueldos:
                print("Primero debe asignar sueldos aleatorios.")
            else:
                sueldo_max, sueldo_min, sueldo_prom, sueldo_geom = calcular_estadisticas(sueldos)
                print("Estadísticas de sueldos:")
                print(f"Sueldo mas alto: ${sueldo_max}")
                print(f"Sueldo mas bajo: ${sueldo_min}")
                print(f"Promedio de sueldos: ${sueldo_prom:.2f}")
                print(f"Media geometrica: ${sueldo_geom:.2f}")              
        elif opcion == '4':
            if not sueldos:
                print("Primero debe asignar sueldos aleatorios.")
            else:
                generar_reporte(sueldos)

        elif opcion == '5':
            print("Finalizando programa...")
            print("Desarrollado por Larry Montecino")
            print("RUT: 20.883.113-5")
            break

        else:
            print("Opción no valida. Por favor, seleccione una opción del menu.")

if __name__ == "__main__":
    main()
