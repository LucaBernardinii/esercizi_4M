class Pagamento:

    def processa_pagamento():
        return "Pagamento."

class CartaDiCredito(Pagamento):
    def __init__(self,nome, conto, data, cvv):
        self.nome = nome
        self.conto = conto
        self.data = data
        self.cvv = cvv

    def processa_pagamento(self):
        return f"Pagamento con Carta di Credito effettuato da {self.nome}."

class PayPal(Pagamento):

    def __init__(self,email, password):
        self.email = email
        self.password = password

    def processa_pagamento(self):
        return f"Pagamento con PayPal per {self.email}."

def effettua_pagamento(metodo_di_pagamento: Pagamento):
    print(metodo_di_pagamento.processa_pagamento())

pagamento_carta = CartaDiCredito("Mario Rossi", "1234 5678 9012 3456", "12/23", "123")
pagamento_paypal = PayPal("mario.rossi@example.com", "password123")

effettua_pagamento(pagamento_carta)
effettua_pagamento(pagamento_paypal)