import Championships
import circuits
import math


def intro():
    print("Pulsa 1 para generar un torneo a partir de una lista")
    print("Pulsa 2 para generar el un torneo de N vueltas de una pool de circuitos")
    print("Pulsa 3 para cambiar ajustes")
    print("Pulsa 4 para volver a imprimir la Lista")
    print("Pulsa 5 para pasar el torneo a la lista de circuitos")
    print("Pulsa 6 para revisar un torneo en concreto")
    print("Pulsa 0 para cerrar el menu")


test = [circuits.nord]
txtchamps = []

def menu():
    global test
    races = 5
    minutes = 20
    distance = 305000
    menu_boolean = True
    intro()
    while menu_boolean:
        a = int(input())
        if a == 1:
            Championships.printchampionship(circuits.f12024, minutes, distance)
        elif a == 2:
            test = Championships.returnchampionship(circuits.circuitos, races)
            Championships.printchampionship(test, minutes, distance)
        elif a == 3:
            races = int(input(f"Numero Carreras (el anterior era {races}): "))
            minutes = int(input(f"Numero Minutos por Carrera Aprox (el anterior era {minutes}): "))
            distance = int(input(f"Numero Distancia Real Carrera (el anterior era {distance}): "))
        elif a == 4:
            cont = 0
            Championships.printchampionship(test, minutes, distance)
        elif a == 5:
            name = input("Introduce un nombre para el campeonato: ")
            with open("CircList.txt", "a") as file:
                cont = 0
                file.write(f"{name} \n")
                for i in test:
                    cont += 1
                    aux = Championships.contador(minutes, distance)
                    file.write(str(i.name))
            print("Hecho!")
        elif a == 6:
            a = circuits.nord
            print(a.id)
        elif a == 0:
            menu_boolean = False
        else:
            print("Introduce un numero correcto")

menu()
