import Championships
import circuits
import math
#F1 Dist 305000
#Championships.Championship(circuits.circuitos, 13, 305000)
#Championships.CustomChampionship(circuits.f12024, 5, 20, 305000)
#Boton Cambiar Ajustes
def intro():
    print("Pulsa 1 para torneo random de una lista de circuitos")
    print("Pulsa 2 para generar el número de vueltas de un torneo ya hecho")
    print("Pulsa 3 para cambiar ajustes")
    print("Pulsa 0 para cerrar el menu")


def ajustes(ra, mi, dis):
    races = ra
    minutes = mi
    distance = dis
def menu():
    races = 5
    minutes = 20
    distance = 305000
    menu_boolean = True
    intro()
    while menu_boolean:
        a = int(input())
        if a == 1:
            Championships.CustomChampionship(circuits.circuitos, races, minutes,  distance)
        elif a == 2:
            Championships.Championship(circuits.f12024, minutes, distance)
        elif a == 3:
            races = int(input("Numero Carreras: "))
            minutes = int(input("Numero Minutos por Carrera Aprox: "))
            distance = int(input("Numero Distancia Real Carrera (305000 para F1): "))
        elif a == 0:
            menu_boolean = False
        else:
            print("Introduce un numero correcto")

menu()
