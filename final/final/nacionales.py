from cliente import Cliente

class Nacionales(Cliente):
    __provincia: str
    __localidad: str
    __codigoPostal: str
    
    def __init__(self, nombre, apellido, email, contrasena, direccionPostal, telefono, provincia, localidad, codigoPostal):
        super().__init__(nombre, apellido, email, contrasena, direccionPostal, telefono)
        self.__provincia = provincia
        self.__localidad = localidad
        self.__codigoPostal = codigoPostal
        
    def getProvincia(self):
        return self.__provincia

    def getLocalidad(self):
        return self.__localidad

    def getCodigoPostal(self):
        return self.__codigoPostal
    
    def __str__(self):
        return f"{self.getNombre()} {self.getApellido()} {self.getEmail()} {self.getContrasena()} {self.getDireccionPostal()} {self.getTelefono()} {self.__provincia} {self.__localidad} {self.__codigoPostal}"
       