class Calc:

    def __init__(self, op, num1, num2) -> None:
        
        self.op = op
        self.num1 = num1
        self.num2 = num2
        
    def calcular(self):
        self.__add() if self.op == 'add' else self.__sub()

    def __add(self):
        
        print(self.num1 + self.num2)

    def __sub(self):

        print(self.num1 - self.num2)


calc1 = Calc('add', 1, 1)
calc1.calcular()

calc2 = Calc('', 1, 1)
calc2.calcular()


