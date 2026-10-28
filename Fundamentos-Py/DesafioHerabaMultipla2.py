class Veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano
    
    def ligar(self):
        print("O veículo está ligado")


class Eletrico:
    def __init__(self, bateria):
        self.bateria = bateria
    
    def status_bateria(self):
        print(f"Bateria em {self.bateria}%")


class Combustao:
    def __init__(self, combustivel):
        self.combustivel = combustivel
    
    def status_combustivel(self):
        print(f"Combustível: {self.combustivel}")
    

class CarroHibrido(Veiculo, Eletrico, Combustao):  
    def __init__(self, marca, ano, bateria, combustivel):
        Veiculo.__init__(self, marca, ano)
        Eletrico.__init__(self, bateria)
        Combustao.__init__(self, combustivel)

    def mostrar_info(self):    
        self.ligar()
        self.status_bateria()
        self.status_combustivel()


carro = CarroHibrido("Toyota", 2022, 80, "Gasolina")
carro.mostrar_info()