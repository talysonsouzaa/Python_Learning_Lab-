numeros = [3, 8, 1, 9, 4, 8, 2]
pares = [numero for numero in numeros if numero % 2 == 0]
impar = [numero for numero in numeros if numero % 2 != 0]



pares.sort()
impar.sort(reverse=True)

print(pares)
print(impar)