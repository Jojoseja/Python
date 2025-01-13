import math
import circuits
import random


def contador(tiempo, dist):
    return tiempo / (90 / dist)

# circ = Numero de circuitos; min = minutos aprox por carrera, siendo 90 min aprox el tiempo real


def returnchampionship(circlist, races):
    newchamp = []
    cont = 0
    a = circlist.copy()
    while cont < races:
        b = random.choice(a)
        if b not in newchamp:
            newchamp.append(b)
            cont += 1
    return newchamp


def printchampionship(circlist, minutes, distance):
    cont = 0
    for i in circlist:
        cont += 1
        total_len = contador(minutes, distance)
        print(f"{cont}. {i.name}, {math.ceil(total_len / i.length)} vueltas")