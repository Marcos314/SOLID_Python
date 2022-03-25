class Pessoa:

    def __init__(self, nome, idade, cpf) -> None:
        
        self.nome = nome
        self.idade = idade
        #self.cpf = cpf
        self.__cpf = cpf # O __ (os 2 underline) está "escondendo" o cpf, deixando de forma privada

    def print_cpf(self):
        print(self.__cpf) # Neste caso, como o __cpf está no contexto da classe, ele consegue ser mostrado

    def correr(self):
        print('Estou Correndo')

    def __apresentar_documento(self): # Entendemos que esse método também é privado
        print(self.__cpf)

    



marcos = Pessoa('Marcos', 27, '05144629148')

print(marcos.nome)
print(marcos.idade)

marcos.print_cpf()

# Fazer marcos.__apresentar_documento() não vai funcionar pois o método é privado
# OUTPUT: AttributeError: 'Pessoa' object has no attribute '__apresentar_documento'
marcos.__apresentar_documento()