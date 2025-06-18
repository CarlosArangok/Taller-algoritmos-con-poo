from cafetera import Cafetera

def menu():
    print("\n--- MENÚ CAFETERA ---")
    print("1. Llenar cafetera")
    print("2. Servir taza")
    print("3. Vaciar cafetera")
    print("4. Agregar café")
    print("5. Mostrar estado de la cafetera")
    print("6. Salir")

def main():
    print("=== INICIO ===")
    opcion_inicial = input("¿Desea personalizar la cafetera? (s/n): ").lower()

    if opcion_inicial == 's':
        capacidad = int(input("Ingrese la capacidad máxima (c.c.): "))
        actual = int(input("Ingrese la cantidad actual de café (c.c.): "))
        cafetera = Cafetera(capacidad, actual)
    else:
        cafetera = Cafetera()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            cafetera.llenarCafetera()
        elif opcion == '2':
            cantidad = int(input("Ingrese la cantidad de café para la taza (c.c.): "))
            cafetera.servirTaza(cantidad)
        elif opcion == '3':
            cafetera.vaciarCafetera()
        elif opcion == '4':
            cantidad = int(input("Ingrese la cantidad de café a agregar (c.c.): "))
            cafetera.agregarCafe(cantidad)
        elif opcion == '5':
            print("\n--- ESTADO DE LA CAFETERA ---")
            print(cafetera.mostrarEstado())
        elif opcion == '6':
            print("Gracias por usar la cafetera.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
