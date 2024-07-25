from edificio import Edificio
from departamento import Departamento

import csv

class Gestor:
    __gestor: list
    
    def __init__(self):
        self.__gestor = []
        
    def inicializar(self):
        archivo = open("C:/Users/danie/Documents/GitHub/u3 poo/ejercicio1/archviocsv/EdificioNorte.csv")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            if len(fila) == 7:
                edificio = Edificio(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]), int(fila[5]))
                self.__gestor.append(edificio)
                
            elif len(fila) == 8:
                dpto = Departamento(int(fila[1]), fila[2], int(fila[3]), int(fila[4]), int(fila[5]), int(fila[6]), float(fila[7]))
                edificio.agregarDepartamento(dpto)
        archivo.close()
                
    def mostrar(self):
        for edificio in self.__gestor:
            print(edificio)
            i=0
            while i < edificio.getCantidadDeDepartamentos():
                print(edificio.getDepartamento(i))
                i+=1
            
    def inciso1(self):
        nom = input("Ingrese el nombre del edificio: ")
        i = 0

        while i < len(self.__gestor) and self.__gestor[i].getNombre() != nom:
            i += 1
        
        if i < len(self.__gestor):
            j = 0
            
            while j < self.__gestor[i].getCantidadDeDepartamentos():
                print(self.__gestor[i].getDepartamento(j))
                j += 1
        else:
            print("Edificio no encontrado.")

    def inciso2(self):
        total = 0
        for edificio in self.__gestor:
            i=0
            while i < edificio.getCantidadDeDepartamentos():
                total += edificio.getDepartamento(i).getSuperficieCubierta()
                i+=1
            print(f"Superficie total del edificio {edificio.getNombre()} : {total}")
            
    def inciso3(self):
        nom = input("Ingrese el nombre : ")
        sup = 0
        
        for edificio in self.__gestor:
            i=0
            while i < edificio.getCantidadDeDepartamentos():
                if edificio.getDepartamento(i).getNyaPropietario() == nom:
                    sup += edificio.getDepartamento(i).getSuperficieCubierta()
                i+=1
        print(f"Superficie de {nom} : {sup}")
                    
        
    def inciso4(self):
        piso = int(input("Ingrese el numero de piso: "))
        c = 0
        for edificio in self.__gestor:
            i=0
            while i < edificio.getCantidadDeDepartamentos():
                if piso == edificio.getDepartamento(i).getNumeroDePiso() and edificio.getDepartamento(i).getCantidadDeHabitaciones() == 3 and edificio.getDepartamento(i).getCantidadDeBanos() > 1:
                    c+=1
                i+=1
        print(f"Edificios con piso {piso} y 3 habitaciones y mas de 1 bano: {c}")
    