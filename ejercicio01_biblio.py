paises = []
contador = 0
while contador < 5:
    paises.append(input("Escribe el nombre de un país: "))
    contador += 1;
print(sorted(paises))