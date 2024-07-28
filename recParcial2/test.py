from lista import Lista

def main():
    lista = Lista()
    
    b= False
    
    while not b:
        print("""0, carga
1, inciso1
2, inciso2
3, inciso3
4, inciso4
5, salir""")
        
        opcion = int(input("Escribe una opcion: "))
        
        if opcion == 0:
            lista.inicializar()
            lista.mostrar()
            
        elif opcion == 1:
            try:
                pos = int(input("Escribe la posicion: "))
                lista.inciso1(pos)
            except ValueError:
                print("ingrese un numero")
            except IndexError as e:
                print(e)
        
        elif opcion == 2:
            try: 
                anio = int(input("Escribe el anio: "))
                lista.inciso2(anio)
            except ValueError:
                print("ingrese un numero ")
                
        elif opcion == 3:
            try:
                carga = int(input("Escribe la capacidad de carga: "))
                lista.inciso3(carga)
            except ValueError:
                print("ingrese un numero ")
                
        elif opcion == 4:
            lista.inciso4()
            
        elif opcion == 5:
            print("Adios")
            b = True
if __name__ == "__main__":
    main()