def metros_a_centimetros(valor_en_metros):
    return valor_en_metros * 100
def area_perimetro_cuadrado(lado):
    area = lado ** 2
    perimetro = 4 * lado
    return area, perimetro
def area_perimetro_rectangulo(largo, ancho):
    area = largo * ancho
    perimetro = 2 * (largo + ancho)
    return area, perimetro
def area_perimetro_circulo(radio):
    import math
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    return area, perimetro

def area_perimetro_triangulo(base, altura, lado1, lado2):
    area = 0.5 * base * altura
    perimetro = base + lado1 + lado2
    return area, perimetro

def area_perimetro_pentagono(lado, apotema):
    area = 0.5 * 5 * lado * apotema
    perimetro = 5 * lado
    return area, perimetro

lado_cuadrado = float(input("Ingresa el lado del cuadrado en metros: "))
largo_rectangulo = float(input("Ingresa el largo del rectángulo en metros: "))
ancho_rectangulo = float(input("Ingresa el ancho del rectángulo en metros: "))
radio_circulo = float(input("Ingresa el radio del círculo en metros: "))
base_triangulo = float(input("Ingresa la base del triángulo en metros: "))
altura_triangulo = float(input("Ingresa la altura del triángulo en metros: "))
lado1_triangulo = float(input("Ingresa el primer lado del triángulo en metros: "))
lado2_triangulo = float(input("Ingresa el segundo lado del triángulo en metros: "))
lado_pentagono = float(input("Ingresa el lado del pentágono en metros: "))
apotema_pentagono = float(input("Ingresa el apotema del pentágono en metros: "))

area, perimetro = area_perimetro_cuadrado(lado_cuadrado)
print(f"\nCuadrado:\nÁrea: {area:.2f} m² | {metros_a_centimetros(area):.2f} cm²\nPerímetro: {perimetro:.2f} m | {metros_a_centimetros(perimetro):.2f} cm")

area, perimetro = area_perimetro_rectangulo(largo_rectangulo, ancho_rectangulo)
print(f"\nRectángulo:\nÁrea: {area:.2f} m² | {metros_a_centimetros(area):.2f} cm²\nPerímetro: {perimetro:.2f} m | {metros_a_centimetros(perimetro):.2f} cm")

area, perimetro = area_perimetro_circulo(radio_circulo)
print(f"\nCírculo:\nÁrea: {area:.2f} m² | {metros_a_centimetros(area):.2f} cm²\nPerímetro: {perimetro:.2f} m | {metros_a_centimetros(perimetro):.2f} cm")

area, perimetro = area_perimetro_triangulo(base_triangulo, altura_triangulo, lado1_triangulo, lado2_triangulo)
print(f"\nTriángulo:\nÁrea: {area:.2f} m² | {metros_a_centimetros(area):.2f} cm²\nPerímetro: {perimetro:.2f} m | {metros_a_centimetros(perimetro):.2f} cm")

area, perimetro = area_perimetro_pentagono(lado_pentagono, apotema_pentagono)
print(f"\nPentágono:\nÁrea: {area:.2f} m² | {metros_a_centimetros(area):.2f} cm²\nPerímetro: {perimetro:.2f} m | {metros_a_centimetros(perimetro):.2f} cm")
