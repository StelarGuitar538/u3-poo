class Empleador:
    __nya: str
    __id = int
    __puesto: str
    
    
    def __init__(self, nya, id, puesto):
        self.__nya = nya
        self.__id = id
        self.__puesto = puesto
        
    def getNya(self):
        return self.__nya
    
    def getId(self):
        return self.__id
    
    def getPuesto(self):
        return self.__puesto
    
    def __str__(self):
        return f"{self.__nya} {self.__id} {self.__puesto}"