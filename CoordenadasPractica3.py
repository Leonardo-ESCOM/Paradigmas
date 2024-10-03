# Función que determina en qué cuadrante o eje se encuentra una coordenada (a, b)
def cuadrante(a, b):
    if a == 0 and b == 0:
        print("La coordenada se encuentra en el origen")
    elif a == 0:
        if b > 0:
            print("La coordenada se encuentra en el eje positivo de las Y")
        else:
            print("La coordenada se encuentra en el eje negativo de las Y")
    elif b == 0:
        if a > 0:
            print("La coordenada se encuentra en el eje positivo de las X")
        else:
            print("La coordenada se encuentra en el eje negativo de las X")
    elif a > 0 and b > 0:
        print("La coordenada se encuentra en el primer cuadrante")
    elif a < 0 and b > 0:
        print("La coordenada se encuentra en el segundo cuadrante")
    elif a < 0 and b < 0:
        print("La coordenada se encuentra en el tercer cuadrante")
    elif a > 0 and b < 0:
        print("La coordenada se encuentra en el cuarto cuadrante")

# Variables
a = 2
b = 4

# Llamada a la función
cuadrante(a, b)
