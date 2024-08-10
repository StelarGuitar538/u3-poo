from gestor import Gestor

def main():
    g = Gestor()
    
    b= False
    
    while b == False:
        print("0. Inicializar \n 1. inciso 1 \n 2. inciso 2 \n 3. inciso 3 \n 4. inciso 4 \n 5. salir")
        
        opcion = int(input("Opcion: "))
        
        if opcion == 0:
            g.inicializar()
            g.mostrar()
            
        elif opcion == 1:
            try:
                pos = int(input("Posicion: "))
                g.inciso1(pos)
            except ValueError:
                print("ingrese un numero valido")
            except IndexError as e:
                print(e)
                
        elif opcion == 2:
            try:
                anio = int(input("Anio: "))
                g.inciso2(anio)
            except ValueError:
                print("ingrese un numero valido")
                
        elif opcion == 3:
            try:
                carga = int(input("Carga: "))
                g.inciso3(carga)
            except ValueError:
                print("ingrese un numero valido")
                
        elif opcion == 4:
            g.inciso4()
        
        elif opcion == 5:
            b = True
            
if __name__ == "__main__":
    main()