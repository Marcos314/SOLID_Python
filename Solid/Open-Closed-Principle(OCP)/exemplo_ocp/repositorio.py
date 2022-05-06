class Repositorio:

    def select(self, db_conn: any) -> None:
        conn = db_conn.connect()
        print('Connected to {}'.format(conn))
        print('Fazendo um SELECT * FROM ...')

        db_conn.desconnect()
    
    def insert(self, db_conn: any) -> None:
        conn = db_conn.connect()
        print('Connected to {}'.format(conn))
        print('Fazendo um INSERT INTO ...')

        db_conn.desconnect()
    
