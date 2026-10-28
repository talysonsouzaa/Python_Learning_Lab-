numeros = set([1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 8])

pares={numero for numero in numeros if numero % 2 == 0}
impares={numero for numero in numeros if numero % 2 != 0}

sorted(pares)
sorted(impares)


print(pares)
print(impares)
print(pares <= numeros)
