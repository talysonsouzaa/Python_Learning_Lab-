from pathlib import Path

#fileNotFoundError = Tentar Abrir arquivo que não existe 
try:
    arquivo = open('talyson.py')
except FileNotFoundError as  exc:
    print("Arquivo não encontrado")
    print(exc)


#tentar abrir uma pasta 
ROOT_PATH = Path(__file__).parent


#Acontece quando você não tem permissão
try:
    arquivo = open(ROOT_PATH / 'NovoDiretorio')
except PermissionError as exc:
    print(f"Não foi possivel abrir {exc}")
    

