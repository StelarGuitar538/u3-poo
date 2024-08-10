from abc import ABC, abstractmethod

class Equipo(ABC):
    __marca: str
    __modelo: str
    __anioFabricacion: int
    __tipoCombustible: str
    __potencia: str
    __capacidadCarga: int
    __tarifaDiaria: float
    __cantidadDias: int
    
    def __init__(self, marca, modelo, anioFabricacion, tipoCombustible, potencia, capacidadCarga, tarifaDiaria, cantidadDias):
        self.__marca = marca
        self.__modelo = modelo
        self.__anioFabricacion = anioFabricacion
        self.__tipoCombustible = tipoCombustible
        self.__potencia = potencia
        self.__capacidadCarga = capacidadCarga
        self.__tarifaDiaria = tarifaDiaria
        self.__cantidadDias = cantidadDias
        
    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    def getAnioFabricacion(self):
        return self.__anioFabricacion

    def getTipoCombustible(self):
        return self.__tipoCombustible

    def getPotencia(self):
        return self.__potencia

    def getCapacidadCarga(self):
        return self.__capacidadCarga

    def getTarifaDiaria(self):
        return self.__tarifaDiaria

    def getCantidadDias(self):
        return self.__cantidadDias
    
    @abstractmethod
    def getPrecio(self):
        pass