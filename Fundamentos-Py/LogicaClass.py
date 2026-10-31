class Aluno():
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = int(nota)

    def StatusAluno(self):
        if self.nota >= 7:
            return f'O aluno: {self.nome}, Está Aprovado!'
        
        elif self.nota < 7 and self.nota >= 5:
            return f'O aluno {self.nome}, Está de Recuperação Final'
        
        else:
            return f'O aluno {self.nome}, Está Reprovado'
        

aluno1 = Aluno("Talyson", 10)

print(aluno1.StatusAluno())