from publicaciones import Publicacion

class cd(Publicacion):
    __tiempoDeReproduccionEnMin: int
    __nombreDelNarrador: str
    
    def __init__(self, titulo, categoria, precio, tiempoDeReproduccionEnMin, nombreDelNarrador):
        super().__init__(titulo, categoria, precio)
        self.__tiempoDeReproduccionEnMin = tiempoDeReproduccionEnMin
        self.__nombreDelNarrador = nombreDelNarrador
        
        
    def getTiempoDeReproduccionEnMin(self):
        return self.__tiempoDeReproduccionEnMin
    
    def getNombreDelNarrador(self):
        return self.__nombreDelNarrador
    
    def mostrar(self):
        print(self.get_titulo())
        print(self.get_categoria())
        print(self.get_precio())
        print(self.__tiempoDeReproduccionEnMin)
        print(self.__nombreDelNarrador)
        
        
    def impVenta(self):
        return self.get_precio() * 1.1