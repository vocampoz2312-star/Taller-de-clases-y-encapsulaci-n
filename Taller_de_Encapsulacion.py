class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        """
        Constructor de la clase CuentaBancaria

        Args:
            titular (str): Nombre del titular de la cuenta
            saldo (float): Saldo inicial de la cuenta (por defecto 0)
        """
        self._titular = titular
        self.saldo = saldo  # Usa el setter para validar desde el inicio

    # --- Propiedad titular (solo lectura) ---
    @property
    def titular(self):
        return self._titular

    # --- Propiedad saldo (lectura y escritura controlada) ---
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = valor

    # --- Métodos de operación ---
    def depositar(self, cantidad):
        if cantidad <= 0:
            return False
        self._saldo += cantidad
        return True

    def retirar(self, cantidad):
        if cantidad <= 0 or cantidad > self._saldo:
            return False
        self._saldo -= cantidad
        return True

    def __str__(self):
        return f"Cuenta de {self._titular} | Saldo: ${self._saldo:.2f}"


# ── Pruebas ──────────────────────────────────────────────────────────────────
def main():
    print("=== Creación de cuentas ===")
    cuenta1 = CuentaBancaria("Ana García", 500)
    cuenta2 = CuentaBancaria("Carlos López")        # saldo inicial = 0
    print(cuenta1)
    print(cuenta2)

    print("\n=== Propiedad titular (solo lectura) ===")
    print(f"Titular cuenta1: {cuenta1.titular}")
    try:
        cuenta1.titular = "Otro Nombre"             # debe fallar
    except AttributeError as e:
        print(f"Error al modificar titular: {e}")

    print("\n=== Depósitos ===")
    print(f"Depositar $200 en cuenta1: {cuenta1.depositar(200)}")   # True
    print(f"Depositar $-50 en cuenta2: {cuenta2.depositar(-50)}")   # False
    print(f"Depositar $0  en cuenta2: {cuenta2.depositar(0)}")      # False
    print(cuenta1)
    print(cuenta2)

    print("\n=== Retiros ===")
    print(f"Retirar $100 de cuenta1: {cuenta1.retirar(100)}")       # True
    print(f"Retirar $999 de cuenta2: {cuenta2.retirar(999)}")       # False (sin fondos)
    print(cuenta1)
    print(cuenta2)

    print("\n=== Setter de saldo con valor negativo ===")
    try:
        cuenta1.saldo = -100
    except ValueError as e:
        print(f"ValueError capturado: {e}")

    print("\n=== Estado final ===")
    print(cuenta1)
    print(cuenta2)


if __name__ == "__main__":
    main()