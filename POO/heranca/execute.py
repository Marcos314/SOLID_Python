class Mae:

    def __init__(self, endereco) -> None:
        self.endereco = endereco
        self.sobrenome = 'Silva'
    
    def comer(self) -> None:
        print('Comendo...')
    
    def estudar(self) -> None:
        print('Estudando...')

# Para termos a ideia da herança, colocamos um parenteses na criação da classe filha e passamos a classe mãe como parâmetro
# Os elementos e comportamentos que estão como públicos na classe Mãe serão passados para a classe filha
class Filha(Mae):

    def __init__(self, endereco) -> None:
        super().__init__(endereco) #Faz uma referência a classe mãe, e o init se refere ao contrutor da classe mãe

    def brincar(self, brinquedo) -> None:
        print('Brincando com {}...'.format(brinquedo))
    
ana = Mae('Rua da Ana')
clara = Filha('Rua da Clara')
clara.brincar('boneca')

print(ana.endereco)
print(clara.endereco)

print(clara.estudar())





        
