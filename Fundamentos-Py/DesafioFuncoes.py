
idade_maior = 18

def verificador():
   if age > idade_maior:
      return f" Maior de idade"
   else:
      return f"Maior de Idade"
   
age = int(input("Qual sua idade? "))
print(verificador())