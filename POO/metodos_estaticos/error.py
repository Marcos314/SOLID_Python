class Error:

    @staticmethod
    def protocolo():
        print('Protocolo apresenta error')

    
    @staticmethod
    def entrada():
        print('Entrada apresenta error')

    
Error.protocolo()
Error.entrada()

# Nesses casos eu não preciso instanciar a classe para usar os métodos estáticos.
