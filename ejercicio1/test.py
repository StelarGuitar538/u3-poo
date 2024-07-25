from gestor import Gestor
from edificio import Edificio

def test():
    g = Gestor()
    
    b= False
    
    while not b:
        print("""0, carga
    1, incisio 1
    2, incisio 2
    3, incisio 3
    4, incisio 4
    5, fin""")
        
        op = int(input("Opcion: "))
        
        if op == 0:
            g.inicializar()
            g.mostrar()
        
        elif op == 1:
            g.inciso1()
        
        elif op == 2:
            g.inciso2()
        
        elif op == 3:
            g.inciso3()
        
        elif op == 4:
            g.inciso4()
        
        elif op == 5:
            b = True
        
if __name__ == "__main__":
    test()