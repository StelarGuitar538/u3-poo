from equipos import Equipo

class Herramientas(Equipo):
    __fuente: str
    
    def __init__(self, marca, modelo, anoFabricacion, combustible, potencia, capacidadCarga, alquilerDiario, diasAlquiler, fuente):
        super().__init__(marca, modelo, anoFabricacion, combustible, potencia, capacidadCarga, alquilerDiario, diasAlquiler)
        self.__fuente = fuente
        
    def getFuente(self):
        return self.__fuente
    
    def __str__(self):
        return f"{self.getMarca()} {self.getModelo()} {self.getAnoFabricacion()} {self.getCombustible()} {self.getPotencia()} {self.getCapacidadCarga()} {self.getAlquilerDiario()} {self.getDiasAlquiler()} {self.__fuente}"
    
    def tarifaAlquiler(self):
        if self.__fuente == "bateria":
            imp = (self.getAlquilerDiario() * self.getDiasAlquiler()) * 1.1
        else:
            imp = self.getAlquilerDiario() * self.getDiasAlquiler()
        return imp
