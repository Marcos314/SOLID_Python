'''Uma ideia para lembrarmos dos getters e setters é pensar em atributos como "estados"'''

class Alarme:

    def __init__(self, estado: bool) -> None:
        self.__estado = estado

    def get_estado(self) -> None:
        return self.__estado
    
    def set_estado(self, valor: bool) -> None:
        self.__estado = valor


    