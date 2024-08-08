from lista import Lista
from cliente import Cliente
from nacionales import Nacionales

def main():
    l = Lista()
    c1 = Cliente("daniel", "daniel", "daniel@gmail.com", "123456", "calle 123", "123456789")
    c2 = Cliente("lucas", "buloz", "lucas@gmail.com", "123456", "calle 123", "123456789")
    n1 = Nacionales("juan", "perez", "juan@gmail.com", "123456", "calle 123", "123456789", "madrid", "madrid", "28001")
    n2 = Nacionales("pancho", "perez", "pancho@gmail.com", "123456", "calle 123", "123456789", "madrid", "madrid", "28001")
    
    b = False
    
    while not b:
        print("1. inicializar \n 2. mostrar \n 3. inciso3")
        
        op = int(input("Opcion: "))
        
        if op == 1:
            l.inicializar(c1)
            l.inicializar(c2)
            l.inicializar(n1)
            l.inicializar(n2)
            print(c1)
            print(c2)
            print(n1)
            print(n2)
            
        elif op == 2:
            l.inciso2()
            
        elif op == 3:
            try:
                pos = int(input("Posicion: "))
                l.inciso3(pos)
            except ValueError:
                print("Posicion inválida")
            except IndexError as e:
                print(e)
if __name__ == "__main__":
    main()
        