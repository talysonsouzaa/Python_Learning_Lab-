from functools import wraps

def verificar_admin(func):
    @wraps(func)
    def verificar(*args, **kwargs):
        usuario = args[0]

        if usuario == 'admin':
           resp = func(*args, **kwargs)
           return resp
        else:
            print(f'Acesso Negado!!!!!')

    return verificar
        
@verificar_admin
def deletar_usuario(usuario):
    print(f'Deletando Usuario....')

deletar_usuario("admin")
deletar_usuario("Carlos")





