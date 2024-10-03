import math

def potencia_mas_cercana(n):
    if n <= 1:
        print("La potencia más cercana al número que ingresó es: 1")
    else:
        i = 0
        while True:
            potencia_de_dos = int(math.pow(2, i))
            if potencia_de_dos >= n:
                valor_mas_bajo = n - int(math.pow(2, i - 1))
                valor_mas_alto = potencia_de_dos - n
                break
            i += 1
        
        # Determinar la potencia más cercana
        potencia_de_dos = int(math.pow(2, i - 1)) if valor_mas_bajo < valor_mas_alto else int(math.pow(2, i))
        print(f"La potencia más cercana al número que ingresó es: {potencia_de_dos}")

# Variables
n = 0

# Llamada a la función
potencia_mas_cercana(n)
