class Frazione:
    def __init__(self, numeratore, denominatore):
        self.numeratore = numeratore
        self.denominatore = denominatore

    def __add__(self, altro:int) -> int:
        return Frazione(self.numeratore + altro.numeratore, self.denominatore)

    def __sub__ (self, altro:int) -> int:
        return Frazione(self.numeratore - altro.numeratore, self.denominatore)
    
    def __mul__ (self, altro:int) -> int:
        return Frazione(self.numeratore * altro.numeratore, self.denominatore * altro.denominatore)

    def __str__ (self) -> str:
        return f"Frazione: ({self.numeratore}, {self.denominatore})"


f1 = Frazione(3, 4)
f2 = Frazione(2, 4)


f3 = f1 + f2
print(f3) 


f4 = f1 - f2
print(f4) 


f5 = f1 * f2
print(f5) 


print(f1)
