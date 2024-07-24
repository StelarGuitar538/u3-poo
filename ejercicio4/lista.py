from  nodo import Nodo
from libro import libro
from cd import cd

class Lista:
    __comienzo: Nodo
    
    def __init__(self):
        self.__comienzo = None
        
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
            print("posicion incorrecta")
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