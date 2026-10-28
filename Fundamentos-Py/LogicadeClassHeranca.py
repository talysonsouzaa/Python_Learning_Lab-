class Pessoa():
    def  __init__(self, nome, idade):
        self.nome = nome
        self.idade = int(idade)

    def apresentar(self):
        return f'Olá meu nome é {self.nome}, e tenho {self.idade} anos de idade'
    
class Aluno(Pessoa):
    def __init__(self, nome, idade, nota):
        super().__init__(nome, idade)
        self.nota = int(nota)
        

    def status(self):
        if self.nota >= 7:
            return f'O aluno {self.nome} esta Aprovado. A nota do mesmo foi {self.nota} \n'
        
        elif self.nota <7 and self.nota>= 5:
            return f'O aluno {self.nome} esta de Recuperação. A nota do mesmo foi {self.nota}! \n'
        
        else:
            return f'O aluno {self.nome} esta Reprovado!. A nota do mesmo foi {self.nota}! \n'


aluno1 = Aluno("Talyson",  21, 8)
aluno2 = Aluno("Mariana", 20, 6)
aluno3 = Aluno("Dony", 46, 4)

print(aluno1.apresentar())
print(aluno1.status())

print(aluno2.apresentar())
print(aluno2.status())

print(aluno3.apresentar())
print(aluno3.status())

