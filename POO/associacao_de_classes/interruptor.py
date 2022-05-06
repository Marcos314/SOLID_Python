from typing import Type
class Interruptor:

    def __init__(self, comodo):
        self._comodo = comodo

    def ascender(self):
        print("Ascendo {}".format(self._comodo))

    def apagar(self):
        print("Apagando {}".format(self._comodo))


class Pessoa:

    def ascender_luz(self, interruptor: Type[Interruptor]):
        interruptor.ascender()

    def apagar_luz(self, interruptor: Type[Interruptor]):
        interruptor.apagar()
    
    def dormir(self):
        print("Dormindo...")


raimundo = Pessoa()
interruptor_quarto = Interruptor("quarto")

`raimundo`.ascender_luz(interruptor_quarto)
raimundo.apagar_luz(interruptor_quarto)
raimundo.dormir()

# Conseguimos com isso fazer a associação das classes Pessoa e Interruptor a partir dos seus objetos.