class Departamento:
    __id: int
    __numeroDePiso: int
    __nyaPropietario: str
    __numeroDeDepartamento: int
    __cantidadDeHabitaciones: int
    __cantidadDeBanos: int
    __superficieCubierta: float
    
    def __init__(self, id, nyaPropietario, numeroDePiso, numeroDeDepartamento, cantidadDeHabitaciones, cantidadDeBanos, superficieCubierta):
        self.__id = id
        self.__nyaPropietario = nyaPropietario
        self.__numeroDePiso = numeroDePiso
        self.__numeroDeDepartamento = numeroDeDepartamento
        self.__cantidadDeHabitaciones = cantidadDeHabitaciones
        self.__cantidadDeBanos = cantidadDeBanos
        self.__superficieCubierta = superficieCubierta
        
    def getId(self):
        return self.__id
    
    def getNyaPropietario(self):
        return self.__nyaPropietario
    
    def getNumeroDePiso(self):
        return self.__numeroDePiso
    
    def getNumeroDeDepartamento(self):
        return self.__numeroDeDepartamento
    
    def getCantidadDeHabitaciones(self):
        return self.__cantidadDeHabitaciones
    
    def getCantidadDeBanos(self):
        return self.__cantidadDeBanos
    
    def getSuperficieCubierta(self):
        return self.__superficieCubierta
    
    def __str__(self):
        return f"{self.__id} {self.__nyaPropietario} {self.__numeroDePiso} {self.__numeroDeDepartamento} {self.__cantidadDeHabitaciones} {self.__cantidadDeBanos} {self.__superficieCubierta}"