from publicaciones import Publicacion
from libro import libro
from cd import cd
from lista import Lista

def test():
    l = Lista()
    libro1 = libro("El libro", "Ficcio", 10.0, "Juan Perez", "2021", 100)
    libro2 = libro("los 3 chanchitos", "novela", 250, "la gorda killer", "2010", 10000)
    cd1 = cd("El cd", "Ficcio", 10.0, 10, "Juan Perez")
    cd2 = cd("El cd", "Ficcio", 10.0, 10, "Juan Perez")
    
    b=True
    
    while b:
        print("0, carga")
        print("1, inciso a")
        print("2, inciso b")
        print("3, inciso c")
        print("4, salir")
        
        opcion = int(input("Elige una opcion: "))
        
        if opcion == 0:
            l.agregar(libro1)
            l.agregar(cd1)
            l.agregar(libro2)
            l.agregar(cd2)
            libro1.mostrar()
            cd1.mostrar()
            libro2.mostrar()
            cd2.mostrar()

        elif opcion == 1:
            try:
                pos = int(input("ingrese la posicion: "))
                l.buscarPos(pos)
            except ValueError:
                print("ingrese un numero valido")
            except IndexError as e:
                print(e)
                
        elif opcion == 2:
            l.cantidad()
            
        elif opcion == 3:
            l.mostrar2()
            
        elif opcion == 4:
            b=False
            
if __name__ == "__main__":
    test()
    