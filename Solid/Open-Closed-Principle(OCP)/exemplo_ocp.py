# A classe Circo atende o princípio da responsabilidade unica, no entando ela não é aberta para extensão. Essa classe já está definida propriamente dita.

# Só é aceito como tipo 1 e tipo 2, caso eu tenha que inserir um outro comportamento nessa classe terei que ALTERAR o código já existente, adicionando um novo tipo.

class Circo:

    def apresentar(self, tipo):
        if tipo == 1:
            self.apresentar_malabarista()
        if tipo == 2:
            self.apresentar_palhaco()
        
    
    def apresentar_malabarista(self):
        print("Malabarista apresentando seu show")
    
    def apresentar_palhaco(self):
        print("Palhaco apresentando seu show")

# Um módulo será considerado aberto se ainda estiver disponível para extensão. Por exemplo, deve ser possível adicionar campos as estruturas de dados que contém ou novos elementos ao conjunt ode funções que executa.


class Circo:

    def apresentar(self, apresentador: any):

        apresentador.apresentar_show()

class Malabarista:

    def apresentar_show(self):
        print("Malabarista apresentando seu show")

class Palhaco:

    def apresentar_show (self):
        print("Palhaco apresentando seu show")