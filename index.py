from Hotels import *
from Barri import *
from Districte import *

def ordenar_per_estrelles(hotels: list[Hotel]) -> list:
    return sorted(hotels, reverse=True, key=lambda x:x.estrelles)

def ordenar_per_nom(hotels: list[Hotel]):
    return sorted(hotels, key=lambda x:x.nom)

def mostrar_noms_hotels(hotels: list):
    for hotel in hotels:
        print(f"{hotel.nom} ({hotel.codi_hotel})")

def buscar_per_nom(hotels: list, nom_a_buscar: str) -> list:
    return [hotel for hotel in hotels if nom_a_buscar.lower() in hotel.nom.lower()]

def buscar_per_estrelles(hotels: list, estrelles: int) -> list:
    return list(filter(lambda x: x.estrelles == estrelles, hotels))

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
    if hotels != []:
        hotel =  min(hotels, key=lambda hotel: hotel.distancia(latitud, longitud))
        return hotel, hotel.distancia(lat, long)
    else:
        return None

def carrers_amb_hotels(hotels: list[Hotel]):
    return list({h.carrer for h in hotels})

def estrelles_per_barri(hotels: list[Hotel], barris: dict[int, Barri]):
    estrelles_barri = {}
    for c_barri, v_barri in barris.items():
        list_estrelles = [0, 0, 0, 0, 0]
        for hotel_in_barri in filter(lambda x: x.codi_barri == c_barri, hotels):
            list_estrelles[hotel_in_barri.estrelles - 1] += 1
        estrelles_barri[v_barri.nom] = list_estrelles
    return estrelles_barri

def densitat_per_districte(hotels: list, barris: dict, districtes: dict) -> dict:
    hotels_dic = dict()
    for codi_barri, barri in barris.items():
        districte = barri.codi_districte
        hotels_barri = [hotel for hotel in hotels if hotel.codi_barri == codi_barri]
        hotels_dic[districte] = hotels_dic.get(districte, 0) + len(hotels_barri)

    def transformar_densitat(info):
        clau_districte, num_hotels = info
        return (clau_districte, num_hotels / districtes[clau_districte].extensio)

    densitats = dict(map(transformar_densitat, hotels_dic.items()))
    return densitats

def afegir_prefixe_int(hotel: Hotel):
    if hotel.telefon[0] != '+':
        hotel.telefon = '+34' + hotel.telefon

def modificar_telefons(hotels: list):
    hotels = list(map(afegir_prefixe_int, hotels))

def mostrar_menu():
    MENU_STRING = """
--- MENÚ PRINCIPAL ---
1 - Veure hotels
2 - Veure hotels per estrelles
3 - Buscar hotels
4 - Buscar hotel proper
5 - Llistat alfabètic d'hotels
6 - Carrers amb hotels
7 - Estadística per barris
8 - Estadística per districtes
9 - Internacionalitzar telèfons
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
            mostrar_hotels(ordenar_per_estrelles(hotels))
        elif opcio == '3':
            buscar_hotels(hotels)
        elif opcio == '4':
            try:
                lat = float(input("Escriu la teva latitud: "))
                long = float(input("Escriu la teva longitud: "))
            except ValueError:
                print("Error: latitud i longitud han de ser valors reals")
            else:
                hotel, distancia = hotel_mes_proper(hotels, lat, long)
                print(f"L'hotel més proper és el {hotel.nom} a {distancia} kms")
        elif opcio == '5':
            llista = ordenar_per_nom(hotels)
            mostrar_hotels(llista)
        elif opcio == '6':
            carrers = carrers_amb_hotels(hotels)
            print(f'Hi ha {len(carrers)} carrers amb algun hotel: {carrers}')
        elif opcio == '7':
            info = estrelles_per_barri(hotels, barris)
            for nom_barri, info_estrelles in info.items():
                print(nom_barri)
                for i in range(len(info_estrelles)):
                    print(f"Hi ha {info_estrelles[i]} hotels de {i+1} estrelles")
                print()
        elif opcio == '8':
            densitats = densitat_per_districte(hotels, barris, districtes)
            for codi, densitat in densitats.items():
                print(f"Districte {codi}: {densitat} hotels/km2")
        elif opcio == '9':
            modificar_telefons(hotels)
        elif opcio == 'S' or opcio == 's':
            print("Sortint del programa...")
        else:
            print("Opcio no permesa")
finally:
    print("© Xavier Martín i Víctor Fernández")