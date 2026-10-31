def gerador_transacoes(numeros: list[int]):
    for numero in numeros:
        if numero >= 0:
         yield f'deposito: {numero}'

g = gerador_transacoes([100, -50, 2000, -30])


for valor in g: 
   print(valor)

