class Capacitacion:
    __nombre: str
    __codigo: str
    __duracion: int
    __matricula: list
    
    def __init__(self, nombre, codigo, duracion):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__duracion = duracion
        self.__matricula = []
        
    def getNombre(self):
        return self.__nombre
    
    def getCodigo(self):
        return self.__codigo
    
    def getDuracion(self):
        return self.__duracion
    
    def __str__(self):
        return f"{self.__nombre} {self.__codigo} {self.__duracion}"