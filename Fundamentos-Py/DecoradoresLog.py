from functools import wraps

def meudec(func):
    @wraps
    def wrapper(*args, **kwargs):
        print("Iniciando")
        resultado = func(*args, **kwargs)
        print("Terminando")

        return resultado
    return wrapper


@meudec
def func():
    print("Exercitando")
    
func()