
def calculador_notas(nome, nota):
    if nota >= 90:
        return f'Olá {nome}, sua nota é A'

    elif nota >= 80:
        return f'Olá {nome}, sua nota é B'

    elif nota >= 70:
        return f'Olá {nome}, sua nota é C'

    elif nota >= 60:
        return f'Olá {nome}, sua nota é D'

    else:
        return f'Olá {nome}, sua nota é F'

nome = input("Qual seu nome? ")
nota = int(input("Qual sua nota? "))

print(calculador_notas(nome, nota))
