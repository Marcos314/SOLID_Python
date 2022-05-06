class Loja:

    tarifa = 1.03

    def __init__(self, endereco: str) -> None:

        self._endereco = endereco

    def apresentar_endereco(self) -> None:
        print(self._endereco)
    
    @classmethod
    def vender(cls) -> int:
        return 40 * cls.tarifa
    
    @classmethod
    def alterar_tarifa(cls, nova_tarifa: int) -> None:
        cls.tarifa = nova_tarifa

loja_praia = Loja('Rua da Praia')
loja_centro = Loja('Rua do Centro')

loja_praia.apresentar_endereco()

print(loja_praia.vender())
print(loja_centro.vender())

loja_centro.alterar_tarifa(2.5)


print(loja_praia.vender())
print(loja_centro.vender())



