class MysqlDB:

    def __init__(self) -> None:

        self.__connection = 'MysqlDB'

    def connect(self) -> str:
        print('Conectando ao banco Mysql...')
        return self.__connection

    def desconnect(self) -> None:
        print('Desconectando do banco Mysql...')
