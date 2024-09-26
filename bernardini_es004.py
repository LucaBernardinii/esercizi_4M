class Calcolatrice:
    
    def __init__(self, num1: int, num2: int):
        self.num1 = num1
        self.num2 = num2

    @staticmethod
    def addizione(num1, num2):
            somma = num1 + num2
            return somma
    
    @staticmethod
    def sottrazione(num1, num2):
            differenza = num1 - num2
            return differenza
    
    @staticmethod
    def moltiplicazione(num1, num2):
            prodotto = num1 * num2
            return prodotto

    @staticmethod
    def divisione(num1, num2):
            if num1 != 0:
                quoziente = num1 / num2
                return quoziente
            else:
                print("Impossibile dividere per 0.")
        

print(Calcolatrice.addizione(10, 5))       
print(Calcolatrice.sottrazione(10, 5))     
print(Calcolatrice.moltiplicazione(10, 5)) 
print(Calcolatrice.divisione(10, 5))       