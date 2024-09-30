class Pagamento:

    def __init__(self, processa_pagamento):
        self.processa_pagamento = processa_pagamento


class CartaDiCredito(Pagamento):

    def __init__(self, processa_pagamento):
        super().__init__(processa_pagamento)
        self.processa_pagamento = processa_pagamento

class PayPal(Pagamento):

    def __init__(self, processa_pagamento):
        super().__init__(processa_pagamento)
        self.processa_pagamento = processa_pagamento


def effettua_pagamento(metodo_di_pagamento: Pagamento):
    metodo_di_pagamento.processa_pagamento()

pagamento_carta = CartaDiCredito("Mario Rossi", "1234 5678 9012 3456", "12/23", "123")
pagamento_paypal = PayPal("mario.rossi@example.com", "password123")

effettua_pagamento(pagamento_carta)  
effettua_pagamento(pagamento_paypal)  

