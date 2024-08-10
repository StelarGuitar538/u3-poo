from equipos import Equipo

class Herramientas(Equipo):
    __fuente: str
    
    def __init__(self, marca, modelo, anioFabricacion, tipoCombustible, potencia, capacidadCarga, tarifaDiaria, cantidadDias, fuente):
        super().__init__(marca, modelo, anioFabricacion, tipoCombustible, potencia, capacidadCarga, tarifaDiaria, cantidadDias)
        self.__fuente = fuente
        
    def getFuente(self):
        return self.__fuente
    
    def __str__(self):
        return f"{self.getMarca()} {self.getModelo()} {self.getAnioFabricacion()} {self.getTipoCombustible()} {self.getPotencia()} {self.getCapacidadCarga()} {self.getTarifaDiaria()} {self.getCantidadDias()} {self.__fuente}"
    
    def getPrecio(self):
        if self.__fuente == "bateria":
            importe = (self.getTarifaDiaria() * self.getCantidadDias()) * 1.1
        else:
            importe = (self.getTarifaDiaria() * self.getCantidadDias())
        return importe