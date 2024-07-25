from ladrillo import Ladrillo
import csv

class GestorLadrillo:
    __ladrillos: list
    
    def __init__(self):
        self.__ladrillos = []
        
    def inicializar(self):
        archivo = open("C:/Users/danie/Documents/GitHub/u3 poo/ejercicio2/archivoscsv/ladrillos.csv", "r")
        reader = csv.reader(archivo)
        for row in reader:
            self.__ladrillos.append(Ladrillo(int(row[0]), int(row[1]), float(row[2]), float(row[3])))
        
    def mostrar(self):
        for l in self.__ladrillos:
            print(l)