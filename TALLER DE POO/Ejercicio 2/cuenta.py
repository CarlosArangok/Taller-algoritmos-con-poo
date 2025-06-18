class Cuenta:
    __contador_cuentas = 100000 

    def __init__(self, documento='', saldo=0.0, interes_anual=0.0):
        Cuenta.__contador_cuentas += 1
        self.__numero_cuenta = Cuenta.__contador_cuentas
        self.__documento = documento
        self.__saldo = saldo
        self.__interes_anual = interes_anual

    def actualizarSaldo(self):
        interes_diario = self.__interes_anual / 365
        self.__saldo += self.__saldo * interes_diario / 100

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
        else:
            print("Cantidad inválida para ingresar.")

    def retirar(self, cantidad):
        if cantidad > self.__saldo:
            print("Fondos insuficientes.")
        elif cantidad > 0:
            self.__saldo -= cantidad
        else:
            print("Cantidad inválida para retirar.")

    def mostrarDatos(self):
        return (f"Número de cuenta: {self.__numero_cuenta}\n"
                f"Documento del cliente: {self.__documento}\n"
                f"Saldo actual: ${self.__saldo:.2f}\n"
                f"Interés anual: {self.__interes_anual}%")

    def get_saldo(self):
        return self.__saldo
