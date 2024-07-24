from abc import abstractmethod

class Equipo:
    __marca: str
    __modelo: str
    __anoFabricacion: int
    __combustible: str
    __potencia: int
    __capacidadCarga: int
    __alquilerDiario: float
    __diasAlquiler: int
    
    def __init__(self, marca, modelo, anoFabricacion, combustible, potencia, capacidadCarga, alquilerDiario, diasAlquiler):
        self.__marca = marca
        self.__modelo = modelo
        self.__anoFabricacion = anoFabricacion
        self.__combustible = combustible
        self.__potencia = potencia
        self.__capacidadCarga = capacidadCarga
        self.__alquilerDiario = alquilerDiario
        self.__diasAlquiler = diasAlquiler
    
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def getAnoFabricacion(self):
        return self.__anoFabricacion
    
    def getCombustible(self):
        return self.__combustible
    
    def getPotencia(self):
        return self.__potencia
    
    def getCapacidadCarga(self):
        return self.__capacidadCarga
    
    def getAlquilerDiario(self):
        return self.__alquilerDiario
    
    def getDiasAlquiler(self):
        return self.__diasAlquiler
    
    def __str__(self):
        return f"{self.__marca} {self.__modelo} {self.__anoFabricacion} {self.__combustible} {self.__potencia} {self.__capacidadCarga} {self.__alquilerDiario} {self.__diasAlquiler}"
    
    @abstractmethod
    def tarifaAlquiler(self):
        pass