##Esercizio 5

def ControlloVocali(riga):
    n_vocali=0
    n_vocali=riga.count('a')+riga.count('e')+riga.count('i')+riga.count('o')+riga.count('u')
    if n_vocali>=3:
        return True
    else:
        return False

def ControlloDoppia(riga):
    n_doppie=0
    i=len(riga)-1
    j=0
    while j<i:
        if riga[j]==riga[j+1]:
            n_doppie+=1
            break
        j+=1
    if n_doppie>0:
        return True
    return False

def ControlloEsclusi(riga):
    esclusioni=True
    if riga.count('ab')>0 or riga.count('cd')>0 or riga.count('pq')>0 or riga.count('xy')>0:
        esclusioni=False
    return esclusioni

def ControllaSuccessive(riga):
    successive=False
    i=len(riga)-3
    j=0
    while j<i:
        if riga[j]==riga[j+2]:
            successive=True
        j+=1
    return successive

def ControllaCoppie(riga):
    coppie=False
    i=len(riga)-3
    j=0
    while j<i:
        if riga[j:j+2] in riga[j+2:]:
            coppie=True
        j+=1
    return coppie


    
file=open("input_es5.txt",'r')
nice_rows=0
n_righe=0
nought_rows=0
nice_rows2=0
nought_rows2=0
for riga in file:
    n_righe+=1
    flg_vocali=ControlloVocali(riga)
    flg_doppie=ControlloDoppia(riga)
    flg_esclusi=ControlloEsclusi(riga)
    flg_pair=ControllaCoppie(riga)
    flg_following=ControllaSuccessive(riga)
    print("------------------------------------------------------")
    print("PAROLA: ",riga)
    print("Caso 1 - Test vocali : ",flg_vocali)
    print("Caso 1 - Test doppie : ",flg_doppie)
    print("Caso 1 - Test esclusioni : ",flg_esclusi)
    print("Caso 2 - Test ripetizioni : ",flg_pair)
    print("Caso 1 - Test caratteri successivi : ",flg_following)
    if flg_vocali==True and flg_doppie==True and flg_esclusi==True:
        nice_rows+=1
    else:
        nought_rows+=1
    if flg_pair==True and flg_following==True:
        nice_rows2+=1
    else:
        nought_rows2+=1
print("------------------------------------------------------")
print("N° righe esaminate caso 1:",n_righe)
print("N° righe nice caso 1: ",nice_rows)
print("N° righe noughty caso 1: ",nought_rows)
print("N° righe esaminate caso 2:",n_righe)
print("N° righe nice caso 2: ",nice_rows2)
print("N° righe noughty caso 2:",nought_rows2)