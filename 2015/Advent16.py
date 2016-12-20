# Advent 16
indizi = {"children":3,'cats':7,'samoyeds':2,'pomeranians':3,'akitas':0,'vizslas':0,'goldfish':5,'trees':3,'cars':2,'perfumes':1}

def confronta_indizio(dizionario,chiave_confronto,valore_confronto):
    return int(dizionario[chiave_confronto])==int(valore_confronto)

def confronta_indizio_2(dizionario,chiave_confronto,valore_confronto):
    if str(chiave_confronto).lower().replace(" ","")=="cats" or str(chiave_confronto).lower().replace(" ","")=="trees":
        return int(dizionario[chiave_confronto])<int(valore_confronto)
    elif str(chiave_confronto).lower().replace(" ","")=="goldfish" or str(chiave_confronto).lower().replace(" ","")=="pomeranians":
        return int(dizionario[chiave_confronto])>int(valore_confronto)
    else:
        return int(dizionario[chiave_confronto])==int(valore_confronto)

with open("input_es16.txt") as f:
    for riga in f.readlines():
        riga=riga.replace(",",":").replace("\n","").replace(" ","")
        valori=riga.split(":")
        n_uncle_Sue=valori[0]
        if confronta_indizio(indizi,valori[1],valori[2]) and confronta_indizio(indizi,valori[3],valori[4]) and confronta_indizio(indizi,valori[5],valori[6]):
            print("La zia Sue nel caso 1 è la n°",str(n_uncle_Sue.replace("Sue","")))
        if confronta_indizio_2(indizi,valori[1],valori[2]) and confronta_indizio_2(indizi,valori[3],valori[4]) and confronta_indizio_2(indizi,valori[5],valori[6]):
            print("La zia Sue nel caso 2 è la n°",str(n_uncle_Sue.replace("Sue","")))