from abc import  abstractmethod

class Equipo:
    __marca: str
    __modelo: str
    __anioFabricacion: int
    __tipoCombustible: str
    __potencia: int
    __capacidadCarga: int
    __alquilerDiario: float
    __cantidadDiasAlquiler: int
    
    def __init__(self, marca, modelo, anioFabricacion, tipoCombustible, potencia, capacidadCarga, alquilerDiario, cantidadDiasAlquiler):
        self.__marca = marca
        self.__modelo = modelo
        self.__anioFabricacion = anioFabricacion
        self.__tipoCombustible = tipoCombustible
        self.__potencia = potencia
        self.__capacidadCarga = capacidadCarga
        self.__alquilerDiario = alquilerDiario
        self.__cantidadDiasAlquiler = cantidadDiasAlquiler
        
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
    
    def getAlquilerDiario(self):
        return self.__alquilerDiario
    
    def getCantidadDiasAlquiler(self):
        return self.__cantidadDiasAlquiler
    
    def __str__(self):
        return f"{self.__marca} {self.__modelo} {self.__anioFabricacion} {self.__tipoCombustible} {self.__potencia} {self.__capacidadCarga} {self.__alquilerDiario} {self.__cantidadDiasAlquiler}"
    
    @abstractmethod
    def importeTotal(self):
        pass
    
    