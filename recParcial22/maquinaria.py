from equipos import Equipo

class Maquinaria(Equipo):
    __tipo: str
    __peso: int
    
    def __init__(self, marca, modelo, anioFabricacion, tipoCombustible, potencia, capacidadCarga, tarifaDiaria, cantidadDias, tipo, peso):
        super().__init__(marca, modelo, anioFabricacion, tipoCombustible, potencia, capacidadCarga, tarifaDiaria, cantidadDias)
        self.__tipo = tipo
        self.__peso = peso
        
    def getTipo(self):
        return self.__tipo

    def getPeso(self):
        return self.__peso
    
    def __str__(self):
        return f"{self.getMarca()} {self.getModelo()} {self.getAnioFabricacion()} {self.getTipoCombustible()} {self.getPotencia()} {self.getCapacidadCarga()} {self.getTarifaDiaria()} {self.getCantidadDias()} {self.__tipo} {self.__peso}"
    
    def getPrecio(self):
        if self.__peso <= 10:
            importe = (self.getTarifaDiaria() * self.getCantidadDias()) 
        else:
            importe = (self.getTarifaDiaria() * self.getCantidadDias()) * 1.2
        return importe