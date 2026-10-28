class animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
            return f"{self.__class__.__name__}:{' , ' .join([f'{chave} = {valor}' 
                                                        for chave, valor in self. __dict__.items()])}"


class ave(animal):
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
        super().__init__(nro_patas)


class mamifero(animal):
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
        super().__init__(nro_patas)



class gato(mamifero):
    pass



class cachorro(mamifero): 
    pass



class leao(mamifero):
    pass


class ornitorrinco( mamifero, ave):
        pass

Gato = gato(4)
print(Gato)