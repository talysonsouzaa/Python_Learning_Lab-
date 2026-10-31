class Cachorro:
    def __init__(self, nome, raca):
            self.nome = nome 
            self.raca = raca

    def latir(self):
          print (f"O {self.nome}, que e da raca {self.raca} e esta latindo \n")


cachorro1 = Cachorro("BRUTUS", "VIRA LATA")
cachorro2 = Cachorro("PRINCESA", "PITBUL")

print(f"{cachorro1.nome}, É meu amigão") 
cachorro1.latir()

print(f"{cachorro2.nome}, É minha amigona") 
cachorro2.latir() 


print("Sistena Calculador em Py")
print("------------------------")


num1 = input("Qual seu primeiro numero? ")
num2 = input("Qual seu segundo numero ? ")

def calculador_py(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)

    except ValueError:
        return f"Sai dai maluco {num1} ou {num2} quebra a regra"
    
    multi = num1 * num2
    soma = num1 + num2
    sub = num1 - num2

    if num2 == 0:
        div = "Divisão não permitida"
    else:
        div = num1 / num2

    return f"Soma: {soma}, Multiplicacao: {multi}, Subtracao: {sub}, Divisao {div}"


resultado = calculador_py(num1, num2)
print(resultado)