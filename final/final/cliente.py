from abc import ABC
class Cliente(ABC):
    __nombre: str
    __apellido: str
    __email: str
    __contrasena: str
    __direccionPostal: str
    __telefono: int
    
    def __init__(self, nombre, apellido, email, contrasena, direccionPostal, telefono):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contrasena = contrasena
        self.__direccionPostal = direccionPostal
        self.__telefono = telefono
        
    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getEmail(self):
        return self.__email

    def getContrasena(self):
        return self.__contrasena

    def getDireccionPostal(self):
        return self.__direccionPostal

    def getTelefono(self):
        return self.__telefono
    
    def __str__(self):
        return f"{self.__nombre} {self.__apellido} {self.__email} {self.__contrasena} {self.__direccionPostal} {self.__telefono}"