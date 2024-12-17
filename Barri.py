class Barri:
    def __init__(self, nom, codi_districte):
        if isinstance(codi_districte, int) and codi_districte > 0:
            self.nom = nom
            self.codi_districte = codi_districte
        else:
            raise TypeError("codi_districte ha de ser un valor enter positiu")
        
    def __str__(self):
        return f"{self.nom} (districte: {self.codi_districte})"        
    

def importar_barris(file_path, separator):
    barris_dic = {}
    lines_read = 0
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            file.readline()
            for line in file:
                line = line.strip()
                camps = line.split(separator)
                barris_dic[int(camps[0])] = Barri(camps[2], int(camps[1]))
                lines_read += 1
    except FileNotFoundError:
        raise FileNotFoundError("fitxer no trobat")
    
    print(f"S'han importat correctament {lines_read} barris")
    return barris_dic