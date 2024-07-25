from lista import Lista


def test():
    lista = Lista()
    
    b= False
    
    while not b:
        print("""0, carga
        1, mostrar posicion
        2, cantidad de herramientas
        3, capacidad de carga
        4, mostrar tarifa alquiler
        5, salir""")
        
        opcion = int(input("Escribe una opcion: "))
        
        if opcion == 0:
            lista.inicializar()
            lista.mostrar()
            
        elif opcion == 1:
            try:
                pos = int(input("Escribe la posicion: "))
                lista.excepcion(pos)
            except ValueError:
                print("ingrese un numero valido")
            except IndexError as e:
                print(e)
                
        elif opcion == 2:
            anio = int(input("Escribe el anio: "))
            lista.inciso2(anio)
            
        elif opcion == 3:
            carga = int(input("Escribe la capacidad de carga: "))
            lista.inciso3(carga)
            
        elif opcion == 4:
            lista.inciso4()
            
        elif opcion == 5:
            print("Adios")
            b = True
        
if __name__ == "__main__":
    test()