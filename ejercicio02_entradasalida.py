import pickle
class Vehiculo:
    marca = "Toyota"

f = open("vehiculo.dat", "r")
e = pickle.load(f)
f.close()
