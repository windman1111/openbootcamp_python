peso = float(input("Introduzca su peso en kg: \n"))
estatura = float(input("Introduzca su estatura en metros: \n"))
imc = peso / (estatura * estatura)
print(f"Su índice de masa corporal es: {round(imc,2)}")