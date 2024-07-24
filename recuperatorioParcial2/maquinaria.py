from equipos import Equipo

class Maquinaria(Equipo):
    __tipoMaquina: str
    __peso: int
    
    def __init__(self, marca, modelo, anoFabricacion, combustible, potencia, capacidadCarga, alquilerDiario, diasAlquiler, tipoMaquina, peso):
        super().__init__(marca, modelo, anoFabricacion, combustible, potencia, capacidadCarga, alquilerDiario, diasAlquiler)
        self.__tipoMaquina = tipoMaquina
        self.__peso = peso
        
    def getTipoMaquina(self):
        return self.__tipoMaquina
    
    def getPeso(self):
        return self.__peso
    
    def __str__(self):
        return f"{self.getMarca()} {self.getModelo()} {self.getAnoFabricacion()} {self.getCombustible()} {self.getPotencia()} {self.getCapacidadCarga()} {self.getAlquilerDiario()} {self.getDiasAlquiler()} {self.__tipoMaquina} {self.__peso}"
    
    def tarifaAlquiler(self):
        if self.__peso <= 10:
            imp = self.getAlquilerDiario() * self.getDiasAlquiler()
        else:
            imp = (self.getAlquilerDiario() * self.getDiasAlquiler()) * 1.2
        return imp