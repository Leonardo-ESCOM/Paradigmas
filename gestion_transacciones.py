class DepositoInvalidoException(Exception):
    """Se lanza cuando el monto a depositar es negativo."""
    pass

class RetiroInvalidoException(Exception):
    """Se lanza cuando el monto a retirar es negativo."""
    pass

class FondosInsuficientesException(Exception):
    """Se lanza cuando el monto a retirar excede el saldo disponible."""
    pass

class CuentaBancaria:
    def __init__(self, numeroCuenta: str, saldo: float):
        self.numeroCuenta = numeroCuenta
        self.saldo = saldo

    def depositar(self, cantidad: float):
        if cantidad < 0:
            raise DepositoInvalidoException("El monto a depositar no puede ser negativo.")
        self.saldo += cantidad

    def retirar(self, cantidad: float):
        if cantidad < 0:
            raise RetiroInvalidoException("El monto a retirar no puede ser negativo.")
        if cantidad > self.saldo:
            raise FondosInsuficientesException("Fondos insuficientes para completar la transacción.")
        self.saldo -= cantidad

    def __str__(self):
        return f"Cuenta {self.numeroCuenta} - Saldo actual: {self.saldo:.2f}"

def main():
    # Crear una instancia de CuentaBancaria
    cuenta = CuentaBancaria(numeroCuenta="123456789", saldo=1000.0)
    print(f"Cuenta creada: {cuenta}")

    while True:
        print("\n--- Operaciones Bancarias ---")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                cantidad = float(input("Ingrese el monto a depositar: "))
                cuenta.depositar(cantidad)
                print(f"Depósito exitoso. {cuenta}")
            elif opcion == "2":
                cantidad = float(input("Ingrese el monto a retirar: "))
                cuenta.retirar(cantidad)
                print(f"Retiro exitoso. {cuenta}")
            elif opcion == "3":
                print(f"Gracias por usar el sistema. Resumen final: {cuenta}")
                break
            else:
                print("Opción inválida. Por favor, intente de nuevo.")
        except DepositoInvalidoException as e:
            print(f"Error: {e}")
        except RetiroInvalidoException as e:
            print(f"Error: {e}")
        except FondosInsuficientesException as e:
            print(f"Error: {e}")
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número válido.")

if __name__ == "__main__":
    main()
