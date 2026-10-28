notas = {
    "Ana": 8,
    "João": 7,
    "Maria": 9
}

#imprimindo nota de joão com o get
print(notas.get("João"))

#adcionando novo aluno com update
notas.update({"Pedro" : 6} )

#adcionando aluno lucas usando setdefault
notas.setdefault("Lucas", 0)

#removendo maria com pop
notas.pop("Maria")

#percorrendo notas dos alunos
for chaves in notas:
    print(chaves, ":", notas[chaves]) 

#Calculando Media
notas.values()
sum(notas.values())
len(notas)
media = sum(notas.values()) / len(notas)
print("Média das notas:", media)



