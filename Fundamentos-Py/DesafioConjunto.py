
palavra1 = set("PythonPython1122")
palavra2 = set("JavaJava2211")

# Letras únicas de cada palavra (diferença simétrica)
unicas = sorted(palavra1 ^ palavra2)
print("Letras únicas:", unicas)

# Letras comuns
comuns = sorted(palavra1 & palavra2)
print("Letras comuns:", comuns)

# Checar subconjunto/superconjunto
print("palavra1 é superset de palavra2?", palavra1.issuperset(palavra2))
print("palavra2 é superset de palavra1?", palavra2.issuperset(palavra1))

# Listas ordenadas separadas
ordenado1 = sorted(palavra1)
ordenado2 = sorted(palavra2)
print("Ordenado palavra1:", ordenado1)
print("Ordenado palavra2:", ordenado2)
