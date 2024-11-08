class ContoBancario:
    def __init__(self, numero_conto, intestatario, saldo):
        self.conto = numero_conto
        self.intestatario = intestatario
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo
    
    def deposita(self, soldi):
        self.__saldo = self.__saldo + soldi

    def preleva(self, soldi):
        self.__saldo = self.__saldo - soldi

conto = ContoBancario("123456789", "Barbara Del Bianco", 5000)
print(conto.get_saldo())

conto.deposita(3000)
print(conto.get_saldo())

conto.preleva(2000)
print(conto.get_saldo())
