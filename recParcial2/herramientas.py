from equipos import Equipo

class Herramientas(Equipo):
    __fuente: str
    
    def __init__(self, fuente, marca, modelo, anioFabricacion, tipoCombustible, potencia, capacidadCarga, alquilerDiario, cantidadDiasAlquiler):
        super().__init__(marca, modelo, anioFabricacion, tipoCombustible, potencia, capacidadCarga, alquilerDiario, cantidadDiasAlquiler)
        self.__fuente = fuente
        
    def getFuente(self):
        return self.__fuente
        
    def __str__(self):
        return f"{self.getMarca()} {self.getModelo()} {self.getAnioFabricacion()} {self.getTipoCombustible()} {self.getPotencia()} {self.getCapacidadCarga()} {self.getAlquilerDiario()} {self.getCantidadDiasAlquiler()} {self.__fuente} "
    
    def importeTotal(self):
        it = 0
        if self.__fuente == "bateria":
            it = (self.getAlquilerDiario() * self.getCantidadDiasAlquiler()) * 1.1
        else:
            it = (self.getAlquilerDiario() * self.getCantidadDiasAlquiler())
        return it