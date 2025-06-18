from cuenta import Cuenta

def menu():
    print("\n--- Menú BancoBlandon ---")
    print("1. Ingresar dinero")
    print("2. Retirar dinero")
    print("3. Actualizar saldo con interés")
    print("4. Mostrar información de la cuenta")
    print("5. Salir")

def main():
    print("=== CREACIÓN DE CUENTA ===")
    documento = input("Ingrese el documento del titular: ")
    saldo = float(input("Ingrese el saldo inicial: "))
    interes = float(input("Ingrese el interés anual (%): "))

    cuenta = Cuenta(documento, saldo, interes)

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            cantidad = float(input("Ingrese cantidad a depositar: "))
            cuenta.ingresar(cantidad)

        elif opcion == '2':
            cantidad = float(input("Ingrese cantidad a retirar: "))
            cuenta.retirar(cantidad)

        elif opcion == '3':
            cuenta.actualizarSaldo()
            print("Saldo actualizado con interés diario.")

        elif opcion == '4':
            print("\n--- DATOS DE LA CUENTA ---")
            print(cuenta.mostrarDatos())

        elif opcion == '5':
            print("Gracias por usar el BancoBlandon.")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()