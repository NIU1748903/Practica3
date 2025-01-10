from math import acos, cos, sin, pi
from typing import Hashable

class Hotel:
    def __init__(self, nom, codi_hotel, carrer, numero, codi_barri, codi_postal, telefon, latitud, longitud, estrelles):
        if type(numero) != int or numero < 0: raise TypeError("numero ha de ser un valor enter positiu")
        if type(codi_barri) != int or codi_barri <= 0: raise TypeError("codi_barri ha de ser un valor enter positiu")
        if type(estrelles) != int or estrelles <= 0: raise TypeError("estrelles ha de ser un valor enter positiu")
        
        if type(longitud) != float: raise TypeError("longitud ha de ser un valor real")
        if type(latitud) != float: raise TypeError("latitud ha de ser un valor real")

        if not (1 <= estrelles <= 5): raise ValueError("estrelles ha de ser un valor entre 1 i 5")
        self.nom = nom
        self.codi_hotel = codi_hotel
        self.carrer = carrer
        self.numero = numero
        self.codi_barri = codi_barri
        self.codi_postal = codi_postal
        self.telefon = telefon
        self.latitud = latitud
        self.longitud = longitud
        self.estrelles = estrelles

    def __str__(self):
        return f"{self.nom} ({self.codi_hotel}) {self.carrer},{self.numero} {self.codi_postal} (barri: {self.codi_barri}) {self.telefon} ({self.latitud},{self.longitud}) {self.estrelles} estrelles"
    
    def __gt__(self, altre_hotel):
        return self.estrelles > altre_hotel.estrelles

    def distancia(self, latitud, longitud):
        if type(latitud) != float: raise TypeError("latitud ha de ser un valor real")
        if type(longitud) != float: raise TypeError("longitud ha de ser un valor real")

        lat1 = self.latitud*(pi/180)
        lon1 = self.longitud*(pi/180)
        latitud *= (pi/180)
        longitud *= (pi/180)

        return acos(sin(lat1)*sin(latitud) + cos(lat1)*cos(latitud)*cos(longitud-lon1))*6378.137
    
def codi_in_llista_hotels(hotels: list[Hotel], codi):
    trobat = False
    i = 0
    while (not trobat) and (i < len(hotels)):
        if hotels[i].codi_hotel == codi:
            return True
        i += 1
    return False

def importar_hotels(nom, car):
    llista_hotels = []
    try:
        fitxer = open(nom, 'r', encoding='utf-8')
    except:
        raise FileNotFoundError("fitxer no trobat")
    else:
        fitxer.readline()
        count = 0
        for linia in fitxer:
            dades = linia[:-1].split(car)
            dades_nom = dades[0].split(' - ')
            if not codi_in_llista_hotels(llista_hotels, dades_nom[1]):
                llista_hotels.append(Hotel(dades_nom[0], dades_nom[1], dades[1], int(dades[2]), int(dades[3]), dades[4], dades[5], float(dades[6])/1000000, float(dades[7])/1000000, int(dades[8])))
                count += 1
    fitxer.close()
    print(f"S'han importat correctament {count} hotels")
    return llista_hotels

def mostrar_hotels(hotels: float) -> Hashable:
    if len(hotels) == 0:
        print("No hi ha hotels")
        return
    
    for h in hotels:
        print(h)