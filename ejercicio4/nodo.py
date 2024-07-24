from publicaciones import Publicacion

class Nodo:
    __publicacion: Publicacion
    __sig: object
    
    def __init__(self, publicacion):
        self.__publicacion = publicacion
        self.__sig = None

    def getPublicacion(self):
        return self.__publicacion

    def getSig(self):
        return self.__sig

    def setSig(self, sig):
        self.__sig = sig