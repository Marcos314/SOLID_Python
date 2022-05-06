class PostgresDB:

    def __init__(self) -> None:

        self.__connection = 'Postgres'

    def connect(self) -> str:
        print('Conectando ao banco Postgres...')
        return self.__connection

    def desconnect(self) -> None:
        print('Desconectando do banco Postgres...')
