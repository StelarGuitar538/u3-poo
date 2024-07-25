from  nodo import Nodo
from libro import libro
from cd import cd

class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __tope: int
    __index: int
    
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__tope = 0
        self.__index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__index == self.__tope:
            self.__actual = self.__comienzo
            self.__index = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato =self.__actual.getPublicacion()
            self.__actual = self.__actual.getSig()
            return dato
        
    def agregar(self, publicacion):
        nodo = Nodo(publicacion)
        nodo.setSig(self.__comienzo)
        self.__comienzo = nodo
        
    def mostrar(self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getPublicacion())
            aux = aux.getSig()
            
    def buscarPos(self, pos):
        aux = self.__comienzo
        i = 0
        while aux != None and i < pos:
            aux = aux.getSig()
            i += 1
            
        if aux == None:
            raise IndexError("Posicion invalida")
        else:
            publi = aux.getPublicacion()
            if isinstance(publi, libro):
                print("es un libro")
            elif isinstance(publi, cd):
                print("es un cd")
                
    def cantidad(self):
        aux = self.__comienzo
        ccd = 0
        cli = 0
        while aux != None:
            publi = aux.getPublicacion()
            if isinstance(publi, cd):
                ccd += 1
            elif isinstance(publi, libro):
                cli += 1
            aux = aux.getSig()
            
        print(f"cantidad de cd: {ccd} \ncantidad de libros: {cli}")
            
    def mostrar2(self):
        aux = self.__comienzo
        while aux != None:
            publi = aux.getPublicacion()
            print(f"{publi.get_titulo()}, {publi.get_categoria()}, {publi.impVenta()}")
            aux = aux.getSig()