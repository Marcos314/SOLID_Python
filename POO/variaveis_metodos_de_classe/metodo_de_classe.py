class MinhaClasse:    

    def __init__(self, estado):
        self.estado = estado
        self.estatico = 'Eu sou estatico' # variável se encontra no contexto da classe

    def mostrar_estatico(self):
        print(self.estatico)
        
    def mudar_estatico(self):
        self.estatico = 'Variável "estatico" alterado a nível de MÉTODO'



ob1 = MinhaClasse(True)
ob2 = MinhaClasse(False)

ob2.mostrar_estatico()
ob1.mudar_estatico()
ob1.mostrar_estatico()


#print(MinhaClasse.estatico)