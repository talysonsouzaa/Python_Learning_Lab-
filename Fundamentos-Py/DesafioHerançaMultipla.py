class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def apresentar(self):
        print(f"Ola meu nome é {self.nome} e tenho {self.idade} anos")


class Funcionario:
    def __init__(self, salario):
        self.salario = salario
   
    def mostrar_salario(self):
        print(f"Meu salario é R$ {self.salario}")


class Estudante:
    def __init__(self, curso):
        self.curso = curso

    def mostrar_curso(self):
        print(f"Estou cursando {self.curso}")


class Estagiario(Pessoa, Funcionario, Estudante):
    def __init__(self, nome, idade, salario, curso):
        Pessoa.__init__(self, nome, idade)
        Funcionario.__init__(self, salario)
        Estudante.__init__(self, curso)

    def mostrar_dados(self):
        self.apresentar()
        self.mostrar_salario()
        self.mostrar_curso()


estagiario = Estagiario("João", 20, 1500, "Informática")
estagiario.mostrar_dados()