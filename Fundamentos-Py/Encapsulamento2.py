class Gato:
    def __init__(self, nome, cor, idade):
        self._nome = nome
        self._cor = cor
        self._idade = idade

    def miar(self):
        return f"Miauuuuu Seu preto"
    
    def dormir(self):
        return f"descançar ne porque o {self._nome} não é de ferro"
    
    def mostrar(self):
        return self._nome, self._cor, self._idade
    
gato = Gato("Arnold", "Preto", 13 )

print(gato.mostrar()) 