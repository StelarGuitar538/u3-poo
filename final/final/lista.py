from cliente import Cliente
from nacionales import Nacionales
from nodo import Nodo

class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __index: int
    __tope: int
    
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__index = 0
        self.__tope = 0
        
    def __iter__(self):
        self.__actual = self.__comienzo
        self.__index = 0
        return self
    
    def __next__(self):
        if self.__index == self.__tope or self.__actual is None:
            raise StopIteration
        else:
            self.__index += 1
            dato = self.__actual.getCliente()
            self.__actual = self.__actual.getSig()
            return dato
        
    def inicializar(self, cliente):
        nodo = Nodo(cliente)
        if self.__comienzo is None:
            self.__comienzo = nodo
        else:
            actual = self.__comienzo
            while actual.getSig() is not None:
                actual = actual.getSig()
            actual.setSig(nodo)
        self.__tope += 1
    
    def inciso2(self):
        for dato in self:
            if isinstance(dato, Nacionales):
                print(dato.getNombre(), dato.getProvincia())
                
    def inciso3(self, pos):
            if pos < 0 or pos >= self.__tope:
               raise IndexError("Posición inválida")
            
            self.__actual = self.__comienzo
            self.__index = 0
            
            while self.__index < pos:
                self.__actual = self.__actual.getSig()
                self.__index += 1
                
            cliente = self.__actual.getCliente()
            if isinstance(cliente, Nacionales):
                print("En dicha posición el Cliente es Nacional")
            elif isinstance(cliente, Cliente):
                print("En dicha posición el Cliente es Local")
