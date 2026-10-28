
class carro:
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo
     
    def __str__(self):
        
        return f"A cor do seu carro é, {self.cor} \nO modelo do seu carro é {self.modelo}"
c1 = carro("Verde", "Palio 2012")



class Pessoas:
    def __init__(self, name, age, cor):
        self.name = name
        self.age = age
        self.cor = cor


    def correr(self):
       return f"To correndo capeta!"    

    def __str__(self):
        return f"{self.__class__.__name__}: {' , ' .join([f'{chave} = {valor}' for chave, valor 
         in self.__dict__.items()])}"


p1 = Pessoas( "Talyson", 20 , "Preto" )
p2 = Pessoas("Talita", 25 , "Branca")



print(p1)
print(p2)
print(p2.correr())