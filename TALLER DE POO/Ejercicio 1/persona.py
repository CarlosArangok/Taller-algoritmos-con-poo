from enum import Enum

class EstadoIMC(Enum):
    BAJO_PESO = -1
    NORMAL = 0
    SOBREPESO = 1
    OBESIDAD = 2
    OBESIDAD_EXTREMA = 3

class Persona:
    __contador_dni = 1

    def __init__(self, documento="", nombre="", edad=0, sexo='M', peso=0.0, altura=0.0):
        self.__documento = documento
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = self.__comprobarSexo(sexo)
        self.__peso = peso
        self.__altura = altura
        self.__dni = self.__generaDNI()

    @classmethod
    def con_documento_nombre_edad_sexo(cls, documento, nombre, edad, sexo):
        return cls(documento, nombre, edad, sexo)

    @classmethod
    def por_defecto(cls):
        return cls()

    def __comprobarSexo(self, sexo):
        if sexo.upper() not in ['M', 'F']:
            return 'M'
        return sexo.upper()

    def __generaDNI(self):
        dni_actual = Persona.__contador_dni
        Persona.__contador_dni += 1
        return dni_actual

    def get_documento(self):
        return self.__documento

    def set_documento(self, documento):
        self.__documento = documento

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def get_sexo(self):
        return self.__sexo

    def set_sexo(self, sexo):
        self.__sexo = self.__comprobarSexo(sexo)

    def get_peso(self):
        return self.__peso

    def set_peso(self, peso):
        self.__peso = peso

    def get_altura(self):
        return self.__altura

    def set_altura(self, altura):
        self.__altura = altura

    def calcularIMC(self):
        if self.__altura <= 0:
            return None

        imc = self.__peso / ((self.__altura / 100) ** 2)
        if imc < 18.5:
            return EstadoIMC.BAJO_PESO
        elif imc <= 24.9:
            return EstadoIMC.NORMAL
        elif imc <= 29.9:
            return EstadoIMC.SOBREPESO
        elif imc <= 39.9:
            return EstadoIMC.OBESIDAD
        else:
            return EstadoIMC.OBESIDAD_EXTREMA

    def esMayorDeEdad(self):
        return self.__edad >= 18

    def listarInformacion(self):
        sexo_str = "Masculino" if self.__sexo == 'M' else "Femenino"
        estado_imc = self.calcularIMC()
        estado_str = estado_imc.name.replace('_', ' ').capitalize() if estado_imc else "No disponible"

        return (
            f"Hola {self.__nombre}, tu código dentro del sistema es {self.__dni}. "
            f"Tu identificación es {self.__documento}. Tu edad es {self.__edad} años. "
            f"Tu género es {sexo_str}. Tu peso es {self.__peso} kg y tu altura es {self.__altura} cm. "
            f"Al calcular tu IMC concluimos que tu peso está: {estado_str}."
        )
