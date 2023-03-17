bisiesto = int(input("Introduce un año y te diremos si es bisiesto: \n"))

def calcular_bisiesto(bisiesto):
    calc_bisi = bisiesto % 4
    if calc_bisi == 0:
        print(f"El año {bisiesto} es bisiesto.")
    else:
        print(f"El año {bisiesto} no es bisiesto")

calcular_bisiesto(bisiesto)