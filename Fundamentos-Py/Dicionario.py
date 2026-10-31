dados = dict(nome="Talyson", idade = 28)
dados["telefone"] = "3344 - 2558"
print(dados)

dados["nome"] = "Mariana"
dados["idade"] = 25
dados ["telefone"] = "5898 - 5202"
print(dados)

for chave, valor in dados.items():
    print(chave, dados["idade"])