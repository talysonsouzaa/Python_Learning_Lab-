import os
import shutil
from pathlib import Path

#pega o caminho e deixa na pasta parente que no caso é a que estamos 
ROOT_PATH = Path(__file__).parent

#Cria arquivos
os.mkdir(ROOT_PATH / "NovoDiretorio")

#abre arquivos e criar com o 'w'
file = open(ROOT_PATH / "NovoArquivo.txt", "w")
file.close()

#renomeia arquivos
os.rename(ROOT_PATH / 'NovoArquivo.txt', ROOT_PATH / 'Alterado.txt')

#remove arquivos
os.remove(ROOT_PATH / 'alterado.txt')

#move arquivos e renoimeia na outra pasta 
shutil.move(ROOT_PATH / 'NovoArquivo.txt', ROOT_PATH / 'NovoDiretorio' /  'novo.txt')