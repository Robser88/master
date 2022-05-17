import random


class Aleatorio:
    def __init__(self):
        self.inicio = 1
        self.fin = 10
        
    def get_Num(self):
        return random.randint(self.inicio, self.fin)
        
    def Iniciar(self):
        Alt_NUm = self.get_Num()
            
        print(f"ingrese un numero del {self.inicio} al {self.fin}")
        
        Num_inten = int(input("Ingrese el numero de intentos: "))    
        intento=0
        while intento < Num_inten:
            
            Ing_Num = int(input("Ingrese el numero por favor: "))
            if Ing_Num == Alt_NUm:
                print(
                    f"El Numero {Ing_Num} es correctolo lograste en tan solo {intento + 1} intento!")
                break
            elif Ing_Num < Alt_NUm:
                print("El Numero es Menor")
            else:
                print("El Numero es Mayor")
            intento += 1
            
            if intento == 3:
                print(f"El Numero correcto es: {Alt_NUm}") 
                
Aleatorio = Aleatorio()
Aleatorio.Iniciar()

            
            