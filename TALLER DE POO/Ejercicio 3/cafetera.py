class Cafetera:
    def __init__(self, capacidadMaxima=1000, cantidadActual=0):
        self.__capacidadMaxima = capacidadMaxima
        self.__cantidadActual = min(cantidadActual, capacidadMaxima)

    def llenarCafetera(self):
        self.__cantidadActual = self.__capacidadMaxima
        print("La cafetera ha sido llenada.")

    def servirTaza(self, cantidad):
        if self.__cantidadActual == 0:
            print("La cafetera está vacía, no se puede servir café.")
        elif cantidad <= self.__cantidadActual:
            self.__cantidadActual -= cantidad
            print(f"Se sirvieron {cantidad} c.c. de café.")
        else:
            print(f"No hay suficiente café. Se sirvieron solo {self.__cantidadActual} c.c.")
            self.__cantidadActual = 0

    def vaciarCafetera(self):
        self.__cantidadActual = 0
        print("La cafetera ha sido vaciada.")

    def agregarCafe(self, cantidad):
        if cantidad <= 0:
            print("Cantidad inválida para agregar.")
            return
        if self.__cantidadActual + cantidad > self.__capacidadMaxima:
            self.__cantidadActual = self.__capacidadMaxima
            print("Se agregó café hasta llenar la cafetera.")
        else:
            self.__cantidadActual += cantidad
            print(f"Se agregaron {cantidad} c.c. de café a la cafetera.")

    def mostrarEstado(self):
        return (f"Capacidad máxima: {self.__capacidadMaxima} c.c.\n"
                f"Cantidad actual: {self.__cantidadActual} c.c.")
