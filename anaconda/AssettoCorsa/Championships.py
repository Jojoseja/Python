import math
import circuits
import random


def contador(tiempo, dist):
    return tiempo / (90 / dist)

# circ = Numero de circuitos; min = minutos aprox por carrera, siendo 90 min aprox el tiempo real
def Championship(circList, min, dist):
    total_len = contador(min, dist)
    cont = 0
    for i in circList:
        cont += 1
        print(f"{cont}. {i.name}, {math.ceil(total_len / i.length)} vueltas")

def CustomChampionship(circList, races, min, dist):
    total_len = contador(min, dist)
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


def ReturnChampionship(circlist, races):
    newchamp = []
    cont = 0
    a = circlist.copy()
    while cont < races:
        b = random.choice(a)
        if b in newchamp:
            print("Hi")
        else:
            newchamp.append(b)
            cont += 1
    return newchamp
