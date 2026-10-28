class veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.rodas = numero_rodas


    def ligando_motor(self):
        print("Ligando motor...")
    
    def __str__(self):
        return f"{self.__class__.__name__}:{" , " .join ([f"{valor}" for valor in self.
                                                          __dict__.items()])}"

    
class motocicleta(veiculo):
    pass


class Carro(veiculo):
    pass


class Caminhao(veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)  
        self.carregado = carregado
    
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Nao' } estou carregado")

    



moto = motocicleta("Preta", "ABC-1234", 2)
carro = Carro("Branco", "XBE-0098", 4)
caminhao = Caminhao("Prata", "RNT-8F82", 8, True)



print(caminhao)
print(carro)
print(moto)
