class Empleado:
    def __init__(self, nombre, id, salario_base):
        self.__nombre = nombre  # Encapsulamiento de atributos
        self.__id = id
        self.__salario_base = salario_base

    # Getters y setters
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_salario_base(self):
        return self.__salario_base

    def set_salario_base(self, salario_base):
        self.__salario_base = salario_base

    # Método para calcular salario (puede ser sobrescrito por clases derivadas)
    def calcular_salario(self):
        return self.__salario_base


class EmpleadoTiempoCompleto(Empleado):
    # Sobrescribe el método para añadir un bono del 10%
    def calcular_salario(self):
        return self.get_salario_base() * 1.1


class EmpleadoMedioTiempo(Empleado):
    # Sobrescribe el método para devolver el 50% del salario base
    def calcular_salario(self):
        return self.get_salario_base() * 0.5


class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, id, salario_base):
        super().__init__(nombre, id, salario_base)
        self.__horas_trabajadas = 0
        self.__tarifa_por_hora = 15  # Tarifa fija por hora

    # Método para establecer las horas trabajadas
    def set_horas_trabajadas(self, horas):
        self.__horas_trabajadas = horas

    def get_horas_trabajadas(self):
        return self.__horas_trabajadas

    # Sobrescribe el método para calcular salario en base a horas trabajadas
    def calcular_salario(self):
        return self.__horas_trabajadas * self.__tarifa_por_hora


# Programa principal
if __name__ == "__main__":
    # Crear una lista de empleados
    empleados = [
        EmpleadoTiempoCompleto("Alice", "TC001", 3000),
        EmpleadoMedioTiempo("Bob", "MT001", 2000),
        EmpleadoPorHoras("Charlie", "PH001", 0),
    ]

    # Establecer las horas trabajadas para el empleado por horas
    empleados[2].set_horas_trabajadas(120)  # Ejemplo: 120 horas trabajadas

    # Mostrar el salario calculado para cada empleado
    for empleado in empleados:
        print(f"Empleado: {empleado.get_nombre()}, ID: {empleado.get_id()}, Salario Calculado: {empleado.calcular_salario():.2f}")
