from functools import reduce

lista = [3,4,5,7,33,4,5,2,22,3,444,554,338,99,65,44345,33224]
filtrada = []
for i in lista:
    if i % 2:
        filtrada.append(i)

print(reduce(lambda a, b: a+b, filtrada))