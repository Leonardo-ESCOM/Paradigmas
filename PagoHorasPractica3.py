# Programa para calcular el pago total de horas trabajadas, incluyendo horas extras
def calcular_pago(horas_trabajadas, sueldo_por_hora):
    # Inicialización de variables
    pago_regular = 0
    pago_extra = 0
    
    # Calcular pago regular y extra
    if horas_trabajadas > 40:
        pago_regular = 40 * sueldo_por_hora
        horas_extras = horas_trabajadas - 40
        pago_extra = horas_extras * sueldo_por_hora * 1.5  # 150% del sueldo base
    else:
        pago_regular = horas_trabajadas * sueldo_por_hora
    
    # Calcular pago total
    pago_total = pago_regular + pago_extra
    
    return pago_regular, pago_extra, pago_total

# Solicitar entrada del usuario
horas_trabajadas = float(input("Introduce el total de horas trabajadas: "))
sueldo_por_hora = float(input("Introduce el sueldo por hora: "))

# Llamada a la función para obtener los resultados
pago_regular, pago_extra, pago_total = calcular_pago(horas_trabajadas, sueldo_por_hora)

# Mostrar los resultados
print(f"Pago regular por las primeras 40 horas: ${pago_regular:.2f}")
print(f"Pago por horas extra: ${pago_extra:.2f}")
print(f"Pago total: ${pago_total:.2f}")
