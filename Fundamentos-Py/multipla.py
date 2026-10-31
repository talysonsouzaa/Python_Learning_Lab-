class animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
            return f"{self.__class__.__name__}:{' , ' .join([f'{chave} = {valor}' 
                                                        for chave, valor in self.__dict__.items()])}"


class ave(animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

    
        
class mamifero(animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

    


class gato(mamifero):
    pass



class cachorro(mamifero): 
    pass



class leao(mamifero):
    pass


class FalarMixin:
    def falar(self):
        return "Opa, Estou Falando!"


class ornitorrinco( mamifero, ave, FalarMixin):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        super().__init__(cor_bico=cor_bico, cor_pelo=cor_pelo, nro_patas=nro_patas )

    
        

Gato = gato(nro_patas=4, cor_pelo="preto")
print(Gato)

perry = ornitorrinco(nro_patas=2, cor_pelo="verde", cor_bico="laranja")
print(perry)

print(perry.falar())