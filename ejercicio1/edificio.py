class Edificio:
    __id: int
    __nombre: str
    __direccion: str
    __empresaConstructora: str
    __cantidadDePisos: int
    __cantidadDeDepartamentos: int
    __departamento: list
    
    def __init__(self, id, nombre, direccion, empresaConstructora, cantidadDePisos, cantidadDeDepartamentos):
        self.__id = id
        self.__nombre = nombre
        self.__direccion = direccion
        self.__empresaConstructora = empresaConstructora
        self.__cantidadDePisos = cantidadDePisos
        self.__cantidadDeDepartamentos = cantidadDeDepartamentos
        self.__departamento = []
        
    def agregarDepartamento(self, departamento):
        self.__departamento.append(departamento)
        
    def __del__(self):
        print("eliminando dpto")
        del self.__departamento
        
    def getId(self):
        return self.__id
    
    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getEmpresaConstructora(self):
        return self.__empresaConstructora
    
    def getCantidadDePisos(self):
        return self.__cantidadDePisos
    
    def getCantidadDeDepartamentos(self):
        return self.__cantidadDeDepartamentos
    
    def getDepartamento(self, id):
        return self.__departamento[id]
    
    def __str__(self):
        return f"{self.__id} {self.__nombre} {self.__direccion} {self.__empresaConstructora} {self.__cantidadDePisos} {self.__cantidadDeDepartamentos}"
