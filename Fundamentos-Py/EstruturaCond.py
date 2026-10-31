MAIOR_IDADE = 18
IDADE_ESPECIAL = 16

idade=int(input("Digite sua idade: "))

if (idade >= MAIOR_IDADE ) and (idade < 120):
    print("Você é maior de idade.")
    print("Pode tirar a carteira de motorista.")

elif (idade >= IDADE_ESPECIAL) and (idade < MAIOR_IDADE):
    print("Você tem idade especial.")
    print("Pode tirar a carteira de motorista com autorização dos pais.")

elif (idade >= 120) or (idade <= 0):
    print("Idade inválida.")

else:
    print("Você é menor de idade.")
    print("Não pode tirar a carteira de motorista.")
