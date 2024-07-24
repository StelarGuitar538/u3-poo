from  nodo import Nodo
from equipos import Equipo
from herramientas import Herramientas
from maquinaria import Maquinaria
import csv

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
            dato = self.__actual.getEquipo()
            self.__actual = self.__actual.getSig()
            self.__indice += 1
            return dato
    
    def agregar(self, equipo):
        nodo = Nodo(equipo)
        nodo.setSig(self.__comienzo)
        self.__comienzo = nodo
        self.__tope += 1
        
    def inicializar(self):
        archivo = open("C:/Users/danie/Documents/GitHub/u3 poo/recuperatorioParcial2/archivoscsv/equipos.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            if fila[0] == "M":
               
               self.agregar(Maquinaria(fila[1], fila[2], int(fila[3]), fila[4], fila[5], int(fila[6]), float(fila[7]), int(fila[8]), fila[9], int(fila[10])))
            elif fila[0] == "E":
                herramienta1 = Herramientas(fila[1], fila[2], int(fila[3]), fila[4], fila[5], (fila[6]), float(fila[7]), int(fila[8]), fila[9])
                self.agregar(herramienta1)
                
    def mostrar(self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getEquipo())
            aux = aux.getSig()
            
    def buscarPos(self, pos):
        self.__actual = 0
        aux = self.__comienzo
        while self.__actual != pos and self.__actual < self.__tope:
            aux = aux.getSig()
            self.__actual += 1
        self.__actual = 0
        return aux.getEquipo()
    
    def excepcion(self, pos):
        if pos >= self.__tope:
            raise IndexError("Posicion invalida")
        else:
            equipo = self.buscarPos(pos)
            if isinstance(equipo, Maquinaria):
                print("es una maquinaria")
            elif isinstance(equipo, Herramientas):
                print("es una herramienta")
                
    def inciso2(self, anio):
        aux = self.__comienzo
        c= 0
        while aux != None:
            equipo = aux.getEquipo()
            if isinstance(equipo, Herramientas) and equipo.getAnoFabricacion() == anio:
                   c += 1
            aux = aux.getSig()
        print(f"Cantidad de maquinarias de {anio}: {c}")
            
            
    def inciso3(self,carga):
        aux = self.__comienzo
        c = 0
        while aux != None:
            equipo = aux.getEquipo()
            if isinstance(equipo, Maquinaria) and equipo.getCapacidadCarga() >= carga:
                c += 1
            aux = aux.getSig()
        print(f"Cantidad de maquinarias con capacidad de carga >= {carga}: {c}")
        
    def inciso4(self):
        for equipo in self:
            print(f"{equipo.getMarca()} {equipo.getModelo()} {equipo.getAnoFabricacion()} {equipo.getCombustible()} {equipo.getPotencia()} {equipo.getCapacidadCarga()} {equipo.tarifaAlquiler()}")
                