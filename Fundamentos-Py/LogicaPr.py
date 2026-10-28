def Nota(name, nota):
    if nota >= 7:
        return f"Ola {name}, Sua nota foi {nota}, E você esta Aprovado"

    elif nota < 7 and nota >= 5 :
        return f"Ola {name}, Sua nota foi {nota}, E você esta de Recuperação"

    else:
        return f"Ola {name}, Sua nota foi {nota}, E você esta Reprovado"

name = input("Qual seu nome?")
nota = int(input("Qual foi sua nota? "))

resultado = Nota(name, nota)
print(resultado)