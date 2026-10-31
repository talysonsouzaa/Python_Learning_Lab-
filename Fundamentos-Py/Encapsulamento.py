class Conta:
    def __init__(self, nmr_agencia, saldo=0):
        self._saldo = saldo
        self.nmr_agencia = nmr_agencia

    def depositar(self, valor):
        #....
        self._saldo += valor

    def sacar(self, valor):
        #....
        self._saldo -= valor 

    def mostrar_saldo(self):
        #....
        return self._saldo


conta = Conta("0001", 100)
conta.depositar(100)

# Errado, Pois esta acioonando o atributo privado diretamente  
print(conta._saldo)

#Certo, criamos um metodo na class que retorn o valor do atributo privado.
print(conta.mostrar_saldo())