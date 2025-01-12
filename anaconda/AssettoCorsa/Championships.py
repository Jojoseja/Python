# Crear Lista de circuitos, en funcion de numero de circuitos
# return ArrayCircuitos + Laps
# DONE Crear Objeto circuitos
import math
import circuits
import random


# circ = Numero de circuitos; min = minutos aprox por carrera, siendo 90 min aprox el tiempo real
def Championship(circList, min, dist):
    def contador(tiempo):
        return tiempo / (90 / dist)
    total_len = contador(min)
    cont = 0
    for i in circList:
        cont += 1
        print(f"{cont}. {i.name}, {math.ceil(total_len / i.length)} vueltas")

def CustomChampionship(circList,races, min, dist):
    def contador(tiempo):
        return tiempo / (90 / dist)
    total_len = contador(min)
    cont = 0
    usedCircuits = []
    while cont < races:
        a = random.choice(circList)
        if a in usedCircuits:
            pass
        else:
            usedCircuits.append(a)
            cont += 1
            print(f"{cont}. {a.name}, {math.ceil(total_len / a.length)} vueltas")
