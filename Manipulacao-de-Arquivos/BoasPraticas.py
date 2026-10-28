from pathlib import Path


ROOT_PATH = Path(__file__).parent

#Não precisa usar o close o arquivo so fica aberto dentro da função, se tentar5 puxar fora ele fecha automatticamente 
with open(ROOT_PATH/'loren.txt', 'r') as arquivo:
    print('Trabalhando com o Arquivo!!!')
print(arquivo.read())

#Verificar se o Arquivo foi aberto com sucesso
try:
   with open(ROOT_PATH/'lloren.txt', 'r') as arquivo:
        print('Trabalhando com o Arquivo!!!')
except IOError as exc:
    print(f"Erro ao Abrir Arquivo{exc}")

#Use a codificação correta
try:
    with open(ROOT_PATH/'loren2.txt', 'w', encoding='utf-8') as arquivo:
        print('Trabalhando com o Arquivo!!!')
except IOError as exc:
        print(f"erro {exc}")