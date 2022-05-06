class Casa:

    def __init__(self) -> None:
        self.__endereco = 'Rua Ana de Fatima Gama Cabral, nº 1'
        self.__proprietario = None
    
    def ascender_luzes(self) -> None:
        print('Ascendo luzes')
    
    def get_endereco(self) -> str:
        return self.__endereco
    
    def set_proprietario(self, proprietario: any) -> None:
        self.__proprietario = proprietario

    def get_proprietario(self) -> any:
        return self.__proprietario
