"""
A classe abaixo segue o Princípio da Responsabilidade Única ela trata apenas de atributos e métodos que dizem respeito a si mesmo,um Veículo.
"""


class Vehicle:
    def __init__(self, year, model, plate_number, current_speed=0) -> None:
        self.year = year
        self.model = model
        self.plate_number = plate_number
        self.current_speed = current_speed

    def move(self):
        self.current_speed += 1

    def accelerate(self, value):
        self.current_speed += value

    def stop(self):
        self.current_speed = 0

    def __str__(self) -> str:
        return f"{self.model}-{self.year}-{self.plate_number}"
