import re


class MinhaClasse:

    # Método construtor
    def __init__(self) -> None:
        
        self.meu_atributo = 'Olá Mundo!'
        

    def meu_metodo(self):
        print('Estou no método!')

    def meu_metodo_2(self, num, mult):
        return num * mult


objeto = MinhaClasse()
objeto.meu_metodo()

result =  objeto.meu_metodo_2(3,4)
print(result)