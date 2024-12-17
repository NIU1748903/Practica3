class Districte:
    def __init__(self, nom, extensio, poblacio):
        if not isinstance(poblacio, int) or poblacio < 0:    
            raise TypeError("poblacio ha de ser un valor enter positiu")
        if not isinstance(extensio, float) or extensio < 0:
            raise TypeError("extensio ha de ser un valor real positiu")
        self.nom = nom
        self.extensio = extensio
        self.poblacio = poblacio
        self.llista_barris = []
    
    def __str__(self):
        string =  f"{self.nom} ({self.extensio} kms2, {self.poblacio} habitants) barris:"
        if len(self.llista_barris) == 0:
            string += " N/D"
        for barri in self.llista_barris:
            string += f" {barri},"
        return string[:-1] if len(self.llista_barris) != 0 else string
    
    def densitat(self):
        return self.poblacio / self.extensio

def importar_districtes(file_path, separator):
    districtes_dic = {}
    lines_read = 0
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            file.readline()
            for line in file:
                line = line.strip()
                camps = line.split(separator)
                districtes_dic[int(camps[0])] = Districte(camps[1], float(camps[2]), int(camps[3]))
                lines_read += 1
    except FileNotFoundError:
        raise FileNotFoundError("fitxer no trobat")
    
    print(f"S'han importat correctament {lines_read} districes")
    return districtes_dic

def omplir_llista_barris(districtes: dict, barris: dict):
    for districte in districtes.values():
        if len(districte.llista_barris) != 0:
            print(len(districte.llista_barris))
            print("El diccionari de districtes ja conté informació dels barris")
            return
    for v in barris.values():
        districtes[v.codi_districte].llista_barris.append(v.nom)