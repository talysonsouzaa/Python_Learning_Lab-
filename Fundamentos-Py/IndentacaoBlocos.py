def sacar(valor):
    saldo = 100
    
    if saldo == valor:
         print("Saque realizado com sucesso.")
         print("Retire seu dinheiro no caixa")
    else:
         print("Saldo insuficiente para saque.")
         print("Por favor, verifique seu saldo e tente novamente.")
    
    print("Obrigado por utilizar nosso serviço.")

def depositar(valor):
    saldo = 100
    saldo += valor
    print("Depósito realizado com sucesso.")


sacar(1000)