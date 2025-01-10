import Championships
import circuits
#F1 Dist 305000
#Championships.Championship(circuits.circuitos, 13, 305000)
#Championships.CustomChampionship(circuits.f12024, 5, 20, 305000)

def menu():
    print("Pulsa 1 para torneo random de una lista de circuitos")
    print("Pulsa 2 para generar el número de vueltas de un torneo ya hecho")
    print("Pulsa 0 para cerrar el menu")
    a = int(input())
    menu_boolean = True
    while menu_boolean:
        if a == 1:
            Championships.CustomChampionship(circuits.circuitos, 13, 20,  305000)
            break
        if a == 2:
            Championships.Championship(circuits.f12024, 20, 305000)
            break
        if a == 0:
            menu_boolean = False
        else:
            print("Introduce un numero correcto")


menu()
