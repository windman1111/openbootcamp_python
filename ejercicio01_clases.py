class Vehiculo:
    def __init__(self, color, puertas, ruedas=4):
        self.color = color
        self.puertas = puertas
        self.ruedas = ruedas

    def mostrar(self):
        print(f"Color: {self.color}")
        print(f"Puertas: {self.puertas}")
        print(f"Ruedas: {self.ruedas}")
        print(f"Velocidad: {self.velocidad}")
        print(f"Cilindrada: {self.cilindrada}")

class Coche(Vehiculo):
    def __init__(self, color, puertas, ruedas, velocidad, cilindrada):
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        super().__init__(color, puertas, ruedas)



coche01 = Coche("blanco", 5, 4, 140, 1500)
coche01.mostrar()