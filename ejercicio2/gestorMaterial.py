from material import Material
import csv

class GestorMaterial:
    __material: list
    
    def __init__(self):
        self.__material = []
        
    def inicializar(self):
        archivo = open("C:/Users/danie/Documents/GitHub/u3 poo/ejercicio2/archivoscsv/materiales.csv", "r")
        reader = csv.reader(archivo)
        for row in reader:
            self.__material.append(Material(int(row[0]), row[1], float(row[2]), float(row[3])))
        
    def mostrar(self):
        for m in self.__material:
            print(m)