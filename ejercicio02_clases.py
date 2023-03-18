
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def mostrar_nota(self):
        if self.nota >= 5:
            print(f"{self.nombre} su nota es {self.nota}. ¡Enhorabuena! Ha aprobado.")
        else:
            print(f"{self.nombre} su nota es {self.nota}. Lo sentimos, ha suspendido.")

alumno01 = Alumno("Andres", 6)
alumno01.mostrar_nota()
