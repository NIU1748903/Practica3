from Hotels import *
from Barri import *
from Districte import *

def ordenar_per_estrelles(hotels: list) -> list:
    return sorted(hotels, reverse=True, key=lambda x:x.nom)

def mostrar_noms_hotels(hotels: list):
    for hotel in hotels:
        print(f"{hotel.nom} ({hotel.codi_hotel})")

def buscar_per_nom(hotels: list, nom_a_buscar: str) -> list:
    return [hotel for hotel in hotels if nom_a_buscar.lower() in hotel.nom.lower()]

def buscar_per_estrelles(hotels: list, estrelles: int) -> list:
    return filter(lambda x: x.estrelles == estrelles, hotels)

def buscar_hotels(hotels: list):
    opc = input("Introdueix criteri de cerca (1 - per nom, 2 - per estrelles): ")
    if opc == "1":
        nom = input("Escriu el nom de l'hotel: ")
        resultat = buscar_per_nom(hotels, nom)
        if resultat == []:
            print("No s'han trobat hotels")
        else:
            print(f"S'han trobat {len(resultat)} hotels")
            mostrar_noms_hotels(resultat)
    elif opc == "2":
        while True:
            try:
                estrelles = int(input("Escriu el nombre d'estrelles: "))
                assert (1 <= estrelles <= 5), "Error: el número d'estrelles ha de ser un valor entre 1 i 5"
                break
            except ValueError:
                print("Error: el número d'estrelles ha de ser un valor enter")
            except AssertionError as missatge:
                print(missatge)
        resultat = buscar_per_estrelles(hotels, estrelles)
        if resultat == []:
            print("No s'han trobat hotels")
        else:
            print(f"S'han trobat {len(resultat)} hotels de {estrelles}")
            mostrar_noms_hotels(resultat)
    else:
        print("Error: criteri de cerca no vàlid")

def hotel_mes_proper(hotels, latitud, longitud):
    return min(hotels, key=lambda hotel: hotel.distancia(latitud, longitud))

def mostrar_menu():
    MENU_STRING = """
--- Menú Principal --- 
1 - Veure hotels
2 - Veure hotels per estrelles
S - Sortir del programa
    """
    print(MENU_STRING)

try:
    hotels = importar_hotels('hotels.csv', ';')
    districtes = importar_districtes('districtes.csv', ';')
    barris = importar_barris('barris.csv', ';')
except FileNotFoundError as missatge:
    print(f"Error llegint fitxers: {missatge}")
except Exception as missatge:
    print(f"Error processant els fitxers: {missatge}")
else:
    print(len(hotels))
    omplir_llista_barris(districtes, barris)
    opcio = 0
    while opcio != 's' and opcio != 'S':
        mostrar_menu()
        opcio = input("Introdueix una opcio: ")
        
        if opcio == '1':
            mostrar_hotels(hotels)
        elif opcio == '3':
            lat = float(input("latitud: "))
            long = float(input("long: "))
            print(hotel_mes_proper(hotels, lat, long))
        elif opcio == 'S' or opcio == 's':
            print("Sortint del programa")
        else:
            print("Opcio no permesa")
finally:
    print("© Xavier Martín i Víctor Fernández")
    
