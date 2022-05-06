'''
Exemplo de código que não está de acordo com o SRP pois apresenta divcisão de responsabilidades ao mesmo tempo
'''

class SistemaCadastralIncorreto:

    def cadastrar(self, nome: str, idade: int) -> None:
        if isinstance(nome, str) and isinstance(idade, int):
            print("Acessando o banco de dados...")
            print(f"Cadastrando {nome} com {idade} anos de idade...")
        else:
            print("Dados inválidos!")

