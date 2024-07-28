from herramientas import Herramientas
from maquinaria import Maquinaria
from nodo import Nodo
import csv

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
            self.__index += 1
            dato = self.__actual.getEquipo()
            self.__actual = self.__actual.getSig()
            return dato
        
    def agregar(self, equipo):
        nodo = Nodo(equipo)
        nodo.setSig(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1
        
    def inicializar(self):
        archivo = open("C:/Users/danie/Documents/GitHub/u3 poo/recParcial2/archivoscsv/equipos.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            if fila[0] == "M":
                nm = Maquinaria(fila[1], fila[2], int(fila[3]), fila[4], fila[5], int(fila[6]), float(fila[7]), int(fila[8]), fila[9], int(fila[10]))
                self.agregar(nm)
            elif fila[0] == "E":
                nh = Herramientas(fila[1], fila[2], int(fila[3]), fila[4], fila[5], (fila[6]), float(fila[7]), int(fila[8]), fila[9])
                self.agregar(nh)
                
    def mostrar(self):
        for equipo in self:
            print(equipo)
            
    def inciso1(self, pos):
        if pos >= self.__tope:
            raise IndexError("Posicion invalida")
        else:
            self.__actual = 0
            aux = self.__comienzo
            while self.__actual != pos and self.__actual < self.__tope:
                aux = aux.getSig()
                self.__actual += 1
            self.__actual = 0
            equipo = aux.getEquipo()
            
            if isinstance(equipo, Maquinaria):
                print(f"el equipo en posicion {pos} es una maquinaria")
            elif isinstance(equipo, Herramientas):
                print(f"el equipo en posicion {pos} es una herramienta")
                
    def inciso2(self, anio):
        c = 0
        for equipo in self:
            if isinstance(equipo, Herramientas) and equipo.getAnioFabricacion() == anio:
                c += 1
        print(f"Cantidad de herramientas de {anio}: {c}")
        
    
    def inciso3(self, carga):
        c=0
        for equipo in self:
            if isinstance(equipo, Maquinaria) and equipo.getCapacidadCarga() >= carga:
                c += 1
        print(f"Cantidad de maquinarias con capacidad de carga >= {carga}: {c}")
        
    def inciso4(self):
        for equipo in self:
            print(f"{equipo.getMarca()} {equipo.getModelo()} {equipo.getAnioFabricacion()} {equipo.getTipoCombustible()} {equipo.getPotencia()} {equipo.getCapacidadCarga()} {equipo.importeTotal()}")
        