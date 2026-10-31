name = input("Qual seu nome? ")
resposta = input("vc quer trabalhar conosco")


def mensagem_sim(name):
    print(f"Olá como você está? " , name )
def mensagem_não(name):
    print("Que pena", name)

if resposta == "sim":
    mensagem_sim(name)
else:
    mensagem_não(name)