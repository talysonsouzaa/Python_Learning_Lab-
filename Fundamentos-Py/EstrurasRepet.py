
# exemplo usando um interavel
texto = input("Informe um texto: ")
vogais = input("Informe as vogais desejadas: ").upper()

for letra in texto:  # Para cada letra que estiver na variável texto, faça
    if letra.upper() in vogais:  # Se a letra (em maiúsculo) estiver na variável vogais
        print(letra, end="")
print()  # adiciona uma quebra de linha



# exemplo usando a função built-in range
for numero in range(0, 11): # Usando o range com o for para imprimir números de 0 a 10
    print(numero, end=' ')

for tabuada in range (5, 51, 5): # 5 == start, 51 == fim, 5 == step
    print (tabuada, end=' ')


# While - exemplo de sistema bancario simples
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
    elif opcao == 0:
        print("Saindo...")
    else:
        print("Opção inválida, tente novamente.")


# Exemplo usando break em um while
while True: # loop infinito
    opcao = int(input("Escolha um numero: "))
    if opcao == 0:
        break # sai do loop
    print("Se fudeo kkkkk")

#Exemplo usando break em um for 
for i in range(10):
    if i == 5:
        break
    print("Se fudeo kkkkk")


# Exemplo usando continue em um while
while True: # loop infinito
    opcao = int(input("Escolha um numero: "))
    if opcao == 0:
        continue # pula para o próximo ciclo do loop
    print("Se fudeo kkkkk")

#Exemplo usando continue em um for 
for i in range(10):
    if i == 5:
        continue
    print("Se fudeo kkkkk")