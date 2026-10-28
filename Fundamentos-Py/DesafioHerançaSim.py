class animal:
    def __init__(self,  especie):
        self.especie = especie

    def falar(self, som):
        self.som = som

    def __str__(self):
        return f"{self.__class__.__name__}:{' , ' .join([f'{chave} = {valor}' for chave, valor in self.
                                                       __dict__.items()])}"
latido = input("Qual Barulho cachorro faz? ")
Miado = input("Qual Barulho gato faz faz? ")

class cachorro(animal):
    pass
    
class gato(animal):
    pass
    
c = cachorro("Budog")
c.falar(latido)
print(c)

g = gato("Gato")
g.falar(Miado)

print(c.especie, ":", c.som)
print(g.especie, ":", g.som)


    