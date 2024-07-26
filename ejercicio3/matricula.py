from empleador import Empleador
from capacitacion import Capacitacion

class Matricula:
    __fecha: str
    __empleado: Empleador
    __capacitacion: Capacitacion
    
    def __init__(self, fecha, empleado, capacitacion):
        self.__fecha = fecha
        self.__empleado = empleado
        self.__capacitacion = capacitacion
        
    def getFecha(self):
        return self.__fecha
    
    def getEmpleado(self):
        return self.__empleado
    
    def getCapacitacion(self):
        return self.__capacitacion
    
    def __str__(self):
        return f"{self.__fecha} {self.__empleado} {self.__capacitacion}"