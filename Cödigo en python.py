from abc import ABC, abstractmethod
# Clase abstracta Vehículo
class Vehículo(ABC):
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    @abstractmethod
    def encender(self):
        pass
    @abstractmethod
    def apagar(self):
        pass
    @abstractmethod
    def describir(self):
        pass
# Clase Auto que hereda de Vehículo
class Auto(Vehículo):
    def encender(self):
        print("El auto ha sido encendido.")
    def apagar(self):
        print("El auto ha sido apagado.")
    def describir(self):
print(f"Este es un auto de marca {self.marca}, modelo {self.modelo}, del año {self.año}.")
# Clase Motocicleta que hereda de Vehículo
class Motocicleta(Vehículo):
    def encender(self):
        print("La motocicleta ha sido encendida.")
    def apagar(self):
        print("La motocicleta ha sido apagada.")
    def describir(self):
        print(f"Esta es una motocicleta de marca {self.marca}, modelo {self.modelo}, del año {self.año}.")
# Clase Camion que hereda de Vehículo
class Camion(Vehículo):
    def encender(self):
        print("El camión ha sido encendido.")
    def apagar(self):
        print("El camión ha sido apagado.")
    def describir(self):
        print(f"Este es un camión de marca {self.marca}, modelo {self.modelo}, del año {self.año}.")
# Programa principal
def main():
    # Lista de vehículos
    vehiculos = [
        Auto("Toyota", "Corolla", 2020),
        Motocicleta("Yamaha", "YZF-R3", 2019),
        Camion("Mercedes-Benz", "Actros", 2021)
    ]
    # Operaciones con cada vehículo
    for vehiculo in vehiculos:
        vehiculo.encender()
        vehiculo.describir()
        vehiculo.apagar()
        print("-" * 30)
if __name__ == "__main__":
    main()
