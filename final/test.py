from lista import Lista
from cliente import Cliente
from nacionales import Nacionales

def main():
    lista = Lista()
    l1 = Cliente("juan", "perez", "juan@juanperez.com", "12345676", "j4000", "264537745")
    l2 = Cliente("diego", "lopez", "diego@diegolopez.com", "12345678", "d7000", "264665799")
    n1 = Nacionales("jose", "reta", "jose@josereta.com", "1234665", "j3000", "264537788", "san juan", "capital", "5400")
    n2 = Nacionales("daniel", "carrascosa", "daniel@danielcarrascosa.com", "144984", "y6000", "264665700", "la rioja", "la rioja", "6800")
    
    b= True
    
    while b:
        print("""1, inciso 1
2, inciso 2
3, inciso 3
4, salir""")
        opcion = int(input("Ingrese la opcion: "))
        if opcion == 1:
            lista.agregar(l1)
            lista.agregar(l2)
            lista.agregar(n1)
            lista.agregar(n2)
            
            lista.mostrar()
        
        elif opcion == 2:
            lista.inciso2()
            
        elif opcion == 3:
            pos = int(input("Ingrese la posicion a buscar: "))
            lista.inciso3(pos)
            
        elif opcion == 4:
            b = False


if __name__ == "__main__":
    main()