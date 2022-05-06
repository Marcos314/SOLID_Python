class MinhaClasse:
    def __init__(self, estado):
        self.estado = estado
    

    @staticmethod
    def metodo_estatico():
        print('Estou no método estático :D')


obj = MinhaClasse(True)
obj.metodo_estatico()

# Podemos usar métodos estaticos como especificadores