class DatabaseConn:

    def __init__(self) -> None: 
        self.__database = 'mysql' # private
        self._conn = '//conn_string' # protected
        self.user = 'root' # public
    

    def get_database(self) -> None:
        print(self.__database)
    
    def _testing_connection(self) -> None:
        print('Testing connection...')
    

class Repository(DatabaseConn):
    def __init__(self) -> None:
        super().__init__()
        # print(self.__database) # error
        print(self.user) # ok
        print(self._conn) # ok


db = DatabaseConn()

# print(db.__database) # error
# print(db._conn)
# print(db.user)
# db._testing_connection()

repo = Repository()

