# Crear Lista de circuitos, en funcion de numero de circuitos
# return ArrayCircuitos + Laps
# DONE Crear Objeto circuitos
import math
import circuits
import random


# circ = Numero de circuitos; min = minutos aprox por carrera, siendo 90 min aprox el tiempo real
def Championship(circ, min):
    def contador(tiempo):
        return tiempo / (90 / 305000)
    total_len = contador(min)
    cont = 0
    for i in range(circ):
        copy = circuits.circuitos
        cont += 1
        a = random.choice(copy)
        b = copy.index(a)
        copy.pop(b)
        print(f"{cont}. {a.name}, {math.ceil(total_len / a.length)} vueltas" )