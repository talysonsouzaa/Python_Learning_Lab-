name = "Talyson"
age = 20
work = "Programador"
linguage = "Python"

print("Olá eu sou o %s. Tenho %d anos e trabalho como %s, " \
"Minha linguagem preferida é %s" % (name, age, work, linguage))


print("Olá eu sou o {3}. Tenho {2} anos e trabalho como {1}, " \
"Minha linguagem preferida é {0}".format (  linguage, work , age,name))

print(f"Olá eu sou o {name}. Tenho {age} anos e trabalho como {work}, " \
f"Minha linguagem preferida é {linguage}")

pi = 3.14159

print(f"O valor de pi {pi: .2f}")

print(f"O valor de pi {pi:10.2f}")