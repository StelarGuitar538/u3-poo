from nodo import Nodo
from nacionales import Nacionales

class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int
    
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0
        
    def __iter__(self):
        self.__actual = self.__comienzo
        self.__indice = 0
        return self
    
    def __next__(self):
        if self.__actual is None:
            raise StopIteration
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            dato = self.__actual.getCliente()
            self.__actual = self.__actual.getSig()
            self.__indice += 1
            return dato
    
    def agregar(self, cliente):
        nodo = Nodo(cliente)
        if self.__comienzo is None:
            self.__comienzo = nodo
        else:
            actual = self.__comienzo
            while actual.getSig() is not None:
                actual = actual.getSig()
            actual.setSig(nodo)
        self.__tope += 1

    def inicializar(self, cliente):
        self.agregar(cliente)
        
    def mostrar(self):
        for i in self:
            print(i)
        
    def inciso2(self):
        for i in self:
            if isinstance(i, Nacionales):
                print(i.getNombre())
                print(i.getProvincia())
            
            
    def inciso3(self, pos):
        aux = self.__comienzo
        self.__actual = 0
    
        while self.__actual != pos and self.__actual < self.__tope:
            aux = aux.getSig()
            self.__actual += 1
            
        if aux is None:
            print("Posicion invalida")
        else:
            cliente = aux.getCliente()
            if isinstance(cliente, Nacionales):
                print(f"la posicion {pos} es de un cliente nacional")
            else:
                print(f"la posicion {pos} es de un cliente local")
                
                