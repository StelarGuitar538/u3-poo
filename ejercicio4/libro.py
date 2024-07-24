from publicaciones import Publicacion

class libro(Publicacion):
    __autor: str
    __fechaDeEdicion: str
    __cantidadDePaginas: int
    
    def __init__(self, titulo, categoria, precio, autor, fechaDeEdicion, cantidadDePaginas):
        super().__init__(titulo, categoria, precio)
        self.__autor = autor
        self.__fechaDeEdicion = fechaDeEdicion
        self.__cantidadDePaginas = cantidadDePaginas

    def get_autor(self):
        return self.__autor

    def get_fechaDeEdicion(self):
        return self.__fechaDeEdicion

    def get_cantidadDePaginas(self):
        return self.__cantidadDePaginas
    
    def mostrar(self):
        print(self.get_titulo())
        print(self.get_categoria())
        print(self.get_precio())
        print(self.__autor)
        print(self.__fechaDeEdicion)
        print(self.__cantidadDePaginas)
        
    
    def impVenta(self):
        fecha = 2024 - int(self.__fechaDeEdicion)
        return (fecha /100) * self.get_precio()