class Pessoas:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age}"

name = input("Qual seu nome? ")
age = int(input("Qual sua idade? "))
p1 = Pessoas( name, age)

print(p1.name,"\n", p1.age)
print(p1)
