class Material:
    __material = int
    __caracteristicas = str
    __cantidad = float
    __costoAdicional = float
    
    def __init__(self, material, caracteristicas, cantidad, costoAdicional):
        self.__material = material
        self.__caracteristicas = caracteristicas
        self.__cantidad = cantidad
        self.__costoAdicional = costoAdicional

    def getMaterial(self):
        return self.__material

    def getCaracteristicas(self):
        return self.__caracteristicas

    def getCantidad(self):
        return self.__cantidad

    def getCostoAdicional(self):
        return self.__costoAdicional
    
    def __str__(self):
        return f"{self.__material} {self.__caracteristicas} {self.__cantidad} {self.__costoAdicional}"
    