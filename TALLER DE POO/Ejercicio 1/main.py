from persona import Persona, EstadoIMC

def pedir_datos():
    documento = input("Ingrese el documento: ")
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    sexo = input("Ingrese el sexo (M/F): ")
    peso = float(input("Ingrese el peso (kg): "))
    altura = float(input("Ingrese la altura (cm): "))
    return documento, nombre, edad, sexo, peso, altura

def main():
    while True:
        print("\n=== Ingreso de persona ===")
        doc, nom, edad, sexo, peso, altura = pedir_datos()

        persona1 = Persona(doc, nom, edad, sexo, peso, altura)
        persona2 = Persona.con_documento_nombre_edad_sexo(doc, nom, edad, sexo)
        persona3 = Persona.por_defecto()
        persona3.set_documento("0000")
        persona3.set_nombre("Por Defecto")
        persona3.set_edad(30)
        persona3.set_sexo('F')
        persona3.set_peso(60)
        persona3.set_altura(160)

        for i, p in enumerate([persona1, persona2, persona3], start=1):
            print(f"\n--- Persona {i} ---")
            estado_imc = p.calcularIMC()
            if estado_imc:
                print(f"IMC: {estado_imc.name.replace('_', ' ').capitalize()}")
            else:
                print("IMC: No se puede calcular")
            print("Mayor de edad:", "Sí" if p.esMayorDeEdad() else "No")
            print(p.listarInformacion())

        continuar = input("\n¿Desea ingresar otra persona? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()
