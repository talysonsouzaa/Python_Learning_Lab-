estoque = {
    "maçã": 10,
    "banana": 5,
    "laranja": 8
}

# 1. Quantidade de banana
print(estoque.get("banana"))

# 2. Adicionar peras
estoque.update({"pera": 10})

# 3. Adicionar uva se não existir
estoque.setdefault("uva", 0)

# 4. Remover laranja
estoque.pop("laranja")

# 5. Estoque atualizado
print(estoque)
