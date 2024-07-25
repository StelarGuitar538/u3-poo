class Ladrillo:
    __alto = 7
    __largo = 25
    __ancho = 15
    __cantidad = int
    __id: int
    __kgMaterialUtilizado = float
    __costo = float
    __material = list
    
    def __init__(self, cantidad, id, l, c):
        self.__cantidad = cantidad
        self.__id = id
        self.__kgMaterialUtilizado = l
        self.__costo = c
        self.__material = []
        
    def getAlto(self):
        return self.__alto

    def getLargo(self):
        return self.__largo

    def getAncho(self):
        return self.__ancho

    def getCantidad(self):
        return self.__cantidad

    def getId(self):
        return self.__id

    def getKgMaterialUtilizado(self):
        return self.__kgMaterialUtilizado

    def getCosto(self):
        return self.__costo 
    
    def agregarMaterial(self, material):
        self.__material.append(material)
    
    def __str__(self):
        return f"{self.__cantidad} {self.__id} {self.__kgMaterialUtilizado} {self.__costo}"