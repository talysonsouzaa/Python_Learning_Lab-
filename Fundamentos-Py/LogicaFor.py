def inverter(lista):
    nova = []

    for i in lista:
        nova.insert(0, i)

    return nova

print(inverter([1, 2, 3, 4]))