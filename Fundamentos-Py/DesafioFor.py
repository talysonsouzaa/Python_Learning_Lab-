
cont_par = 0
cont_impar = 0

for i in range(5):
    numero = int(input("Digite seu numero: "))
    if numero % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1

print("Pares:", cont_par)
print("Ímpares:", cont_impar)



