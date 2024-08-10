from maquinaria import Maquinaria
from herramientas import Herramientas
from nodo import Nodo
import csv

class Gestor:
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
        self.__actual = self.__comienzo
        self.__index = 0
        return self
    
    def __next__(self):
        if self.__actual == None:
            raise StopIteration
        if self.__index == self.__tope:
            self.__actual = self.__comienzo
            self.__index = 0
            raise StopIteration
        else:
            dato = self.__actual.getEquipo()
            self.__actual = self.__actual.getSig()
            self.__index += 1
            return dato
        
    def agregar(self, equipo):
        nodo = Nodo(equipo)
        nodo.setSig(self.__comienzo)
        self.__comienzo = nodo
        self.__tope += 1
        
    def inicializar(self):
        archivo = open("C:/Users/danie/OneDrive/Documentos/GitHub/u3-poo/recParcial22/archivoscsv/equipos.csv", "r")
        reader = csv.reader(archivo, delimiter=';')
        for row in reader:
            if row[0] == "M":
                self.agregar(Maquinaria(row[1], row[2], int(row[3]), row[4], row[5], int(row[6]), float(row[7]), int(row[8]), row[9], int(row[10])))
                
            elif row[0] == "E":
                self.agregar(Herramientas(row[1], row[2], int(row[3]), row[4], row[5], (row[6]), float(row[7]), int(row[8]), row[9]))
        archivo.close()
        
    def mostrar(self):
        for i in self:
            print(i)
        
    def inciso1(self, pos):
        if pos >= self.__tope:
            raise IndexError("Posicion invalida")
        else:
            self.__actual = 0
            aux = self.__comienzo
            while self.__actual != pos and self.__actual < self.__tope:
                self.__actual += 1
                aux = aux.getSig()
            self.__actual = 0
            if isinstance(aux.getEquipo(), Maquinaria):
                print("es una maquinaria")
            elif isinstance(aux.getEquipo(), Herramientas):
                print("es una herramientas")
                    
    def inciso2(self, anio):
        c=0
        for i in self:
            if isinstance(i, Herramientas) and i.getAnioFabricacion() == anio:
                c+=1
        print(f"Cantidad de maquinarias de {anio}: {c}")
        
    def inciso3(self,carga):
        c = 0
        for i in self:
            if isinstance(i, Maquinaria) and i.getCapacidadCarga() >= carga:
                c += 1
        print(f"Cantidad de maquinarias con capacidad de carga >= {carga}: {c}")
        
    def inciso4(self):
        for i in self:
            print(f"{i.getMarca()} {i.getModelo()} {i.getAnioFabricacion()} {i.getTipoCombustible()} {i.getPotencia()} {i.getCapacidadCarga()} {i.getPrecio()}")