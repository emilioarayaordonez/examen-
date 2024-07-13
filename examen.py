import random
import csv

# Lista de nombres de empleados
trabajadores = [
    "Juan Pérez", "María García", "Carlos López", "Ana Martínez",
    "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez",
    "Isabel Gómez", "Francisco Díaz", "Elena Fernández"
]

# Función para generar sueldos aleatorios
def generar_sueldos_aleatorios():
    return [random.randint(300000, 2500000) for _ in range(len(trabajadores))]

# Función para clasificar sueldos
def clasificar_sueldos(sueldos):
    sueldos_clasificados = {"Menor a 800000": [], "Entre 800000 y 2000000": [], "Mayor a 2000000": []}
    for nombre, sueldo in zip(trabajadores, sueldos):
        if sueldo < 800000:
            sueldos_clasificados["Menor a 800000"].append((nombre, sueldo))
        elif 800000 <= sueldo <= 2000000:
            sueldos_clasificados["Entre 800000 y 2000000"].append((nombre, sueldo))
        else:
            sueldos_clasificados["Mayor a 2000000"].append((nombre, sueldo))
    return sueldos_clasificados

# Función para calcular estadísticas
def calcular_estadisticas(sueldos):
    sueldo_maximo = max(sueldos)
    sueldo_minimo = min(sueldos)
    promedio_sueldos = sum(sueldos) / len(sueldos)
    media_geometrica = (sueldo_maximo * sueldo_minimo) ** 0.5
    return sueldo_maximo, sueldo_minimo, promedio_sueldos, media_geometrica

# Función para generar el reporte de sueldos
def generar_reporte(sueldos):
    descuento_salud = 0.07
    descuento_afp = 0.12
    sueldos_reporte = []
    for nombre, sueldo in zip(trabajadores, sueldos):
        descuento_salud_actual = round(sueldo * descuento_salud, 2)
        descuento_afp_actual = round(sueldo * descuento_afp, 2)
        sueldo_liquido = round(sueldo - descuento_salud_actual - descuento_afp_actual, 2)
        sueldos_reporte.append((nombre, sueldo, descuento_salud_actual, descuento_afp_actual, sueldo_liquido))
    
    # Exportar a archivo CSV
    with open("reporte_sueldos.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        writer.writerows(sueldos_reporte)

# Menú principal
def main():
    sueldos = generar_sueldos_aleatorios()
    sueldos_clasificados = clasificar_sueldos(sueldos)
    sueldo_max, sueldo_min, promedio, media_geom = calcular_estadisticas(sueldos)

    while True:
        print("\nMenú:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Generar reporte de sueldos")
        print("5. Salir del programa")

        opcion = int(input("Ingrese la opción deseada: "))
        if opcion == 1:
            sueldos = generar_sueldos_aleatorios()
            print("Sueldos aleatorios generados:", sueldos)
        elif opcion == 2:
            sueldos_clasificados = clasificar_sueldos(sueldos)
            for clasificacion, empleados in sueldos_clasificados.items():
                print(f"\n{clasificacion} TOTAL: {len(empleados)}")
                for nombre, sueldo in empleados:
                    print(f"{nombre}: ${sueldo}")
        elif opcion == 3:
            sueldo_max, sueldo_min, promedio, media_geom = calcular_estadisticas(sueldos)
            print(f"Sueldo más alto: ${sueldo_max}")
            print(f"Sueldo más bajo: ${sueldo_min}")
            print(f"Promedio de sueldos: ${promedio:.2f}")
            print(f"Media geométrica: ${media_geom:.2f}")
        elif opcion == 4:
            generar_reporte(sueldos)
            print("Reporte de sueldos generado en 'reporte_sueldos.csv'")
        elif opcion == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

# Ejecutar el menú principal
main()
