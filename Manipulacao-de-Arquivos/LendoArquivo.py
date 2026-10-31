#abre o arquivo, O r é pra reconhecer as barras
file = open(r'C:\Users\Talyson Negrao\OneDrive\Documentos\Dev\Estudos\Python\Manipulação de Arquivos\loren.txt', 'r')

#Metodo Read le todo o txt
print(file.read())

#Metodo readline le uma linha por vez
print(file.readline())
print(file.readline())

#readlines retorna uma lista do arquivo
print(file.readlines())

#meolhor jeiro de usar readline
for linha in file.readlines():
    print(linha)

#Dica: Enquanto linha for diferente de file.readline() == Vazio, Printa a linha 
while len(linha != file.readline()):
    print(linha)

file.close()