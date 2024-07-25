from gestorLadrillo import GestorLadrillo
from gestorMaterial import GestorMaterial

def test():
    g = GestorLadrillo()
    gm = GestorMaterial()
    
    b= False
    
    while not b:
        print("""0, carga
    1, material
    2, ladrillos""")
        
        op = int(input("Opcion: "))
        
        if op == 0:
            g.inicializar()
            gm.inicializar()
            g.mostrar()
            gm.mostrar()
        
if __name__ == "__main__":
    test()