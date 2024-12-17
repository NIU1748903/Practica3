from Hotels import *
from Barri import *
from Districte import *

def ordenar_per_estrelles(hotels: list) -> list:
    return sorted(hotels, reverse=True, key=lambda x:x.nom)

def mostrar_noms_hotels(hotels: list) -> list:
    for hotel in hotels:
        print(f"{hotel.nom} ({hotel.codi_hotel})")

def buscar_per_nom(hotels: list, nom_a_buscar: str) -> list:
    return [hotel for hotel in hotels if nom_a_buscar.lower() in hotel.nom.lower()]

def buscar_per_estrelles(hotels: list, estrelles: int) -> list:
    return None if not (1 <= estrelles <= 5) else filter(lambda x: x.estrelles == estrelles, hotels)

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
        elif opcio == '2':
            estrelles = int(input("Introdueix el nom a buscar: "))
            mostrar_noms_hotels(buscar_per_estrelles(hotels, estrelles))
        elif opcio == 'S' or opcio == 's':
            print("Sortint del programa")
        else:
            print("Opcio no permesa")
finally:
    print("© Xavier Martín i Víctor Fernández")
    
