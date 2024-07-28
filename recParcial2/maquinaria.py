from equipos import Equipo

class Maquinaria(Equipo):
    __tipoMaquinaria: str
    __peso: int
    
    def __init__(self, tipoMaquinaria, peso, marca, modelo, anioFabricacion, tipoCombustible, potencia, capacidadCarga, alquilerDiario, cantidadDiasAlquiler):
        super().__init__(marca, modelo, anioFabricacion, tipoCombustible, potencia, capacidadCarga, alquilerDiario, cantidadDiasAlquiler)
        self.__tipoMaquinaria = tipoMaquinaria
        self.__peso = peso
        
    def getTipoMaquinaria(self):
        return self.__tipoMaquinaria
    
    def getPeso(self):
        return self.__peso
        
    def __str__(self):
        return f"{self.getMarca()} {self.getModelo()} {self.getAnioFabricacion()} {self.getTipoCombustible()} {self.getPotencia()} {self.getCapacidadCarga()} {self.getAlquilerDiario()} {self.getCantidadDiasAlquiler()} {self.__tipoMaquinaria} {self.__peso} "
    
    def importeTotal(self):
        it = 0
        if self.__peso <= 10:
            it = (self.getAlquilerDiario() * self.getCantidadDiasAlquiler())
        else:
            it = (self.getAlquilerDiario() * self.getCantidadDiasAlquiler()) * 1.2
        return it