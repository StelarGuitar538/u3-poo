from abc import  abstractmethod

class Publicacion:
    __titulo: str
    __categoria: str
    __precio: float
    
    def __init__(self, titulo, categoria, precio):
        self.__titulo = titulo
        self.__categoria = categoria
        self.__precio = precio

    def get_titulo(self):
        return self.__titulo

    def get_categoria(self):
        return self.__categoria

    def get_precio(self):
        return self.__precio
    
    def mostrar(self):
        print(self.__titulo)
        print(self.__categoria)
        print(self.__precio)
    
    
    @abstractmethod
    def getImpVenta(self):
        pass