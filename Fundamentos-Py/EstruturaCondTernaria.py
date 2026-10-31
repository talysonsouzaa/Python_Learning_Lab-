
resposta = input("Você gosta de programação? (s/n): ")

if resposta == 's':
    print ("Legal, Bora estudar para virar um dev!")
    lingua = input ("Qual area vc linguagem dessas vc masi gosta Python, JavaScript, C#?")
    if lingua == 'Python':
            print("Legal, Python é uma excelente linguagem!")
    elif lingua == 'JavaScript':
            print("Ótimo, JavaScript é muito usado para desenvolvimento web!")
    else:
            print("Legal, C# é uma excelente linguagem!")
else: 
    print("Qu pena, vc é uma mula!")