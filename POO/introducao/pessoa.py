class Pessoa: # Nomear classes/atributos com Substantivo

    def __init__(self, nome: str, idade: int) -> None:
        
        self.nome = nome # Nomear classes/atributos com Substantivo
        self.idade = idade # Nomear classes/atributos com Substantivo

    def dirigir(self, veiculo: str) -> None: # Nomear métodos com Verbos
        print('Dirigindo um(a) {}'.format(veiculo))

    def cantar(self) -> None: # Nomear métodos como Verbos
        print('Estou Cantando')

    def apresentar_idade(self) -> int: 
        return self.idade