class MinhaClasse:

    estatico = 'Eu sou estatico' # variável se encontra no contexto da classe

    def __init__(self, estado):
        self.estado = estado

ob1 = MinhaClasse(True)
ob2 = MinhaClasse(False)

print("Variáveis sem modificações")
print(ob1.estatico)
print(ob2.estatico)
print(MinhaClasse.estatico)

'''Mudando a variável estatico no contexto apenas do objeto ob1'''
print("\nMudando a variável estatico no contexto apenas do objeto ob1")

ob1.estatico = 'Variável "estatico" do OB1 alterada'

print(ob1.estatico)
print(ob2.estatico)
print(MinhaClasse.estatico)

'''Mudando a variável estatico no contexto da classe'''
print("\nMudando a variável estatico no contexto da classe")

MinhaClasse.estatico = 'Variável "estatico" da CLASSE alterada'

print(ob1.estatico) # Nesse caso a variável estatica do objeto ob1 não muda
print(ob2.estatico)
print(MinhaClasse.estatico)


ob1 = MinhaClasse(True)
print("\nob1 sendo instanciado novamente")
print(ob1.estatico)
