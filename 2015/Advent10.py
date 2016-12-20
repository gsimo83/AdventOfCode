## Esercizio giorno 10

input_text="1113222113"

#caso 1 
n_passaggi1=40
#caso 2
n_passaggi=50


def ContaCaratteriUguali(Carattere,Testo):
    global start
    i=start
    n_uguali=0
    while i<(len(Testo))and Testo[i]==Carattere:
        n_uguali+=1
        i+=1
        start=i
    return str(n_uguali)+str(Carattere)


#print(len(input_text))
passaggi=0
nuova=""
risultato_40=""
while passaggi<n_passaggi:
    start=0
    while start <= (len(input_text)-1):
        nuova = nuova + ContaCaratteriUguali(input_text[start],input_text)
    input_text=nuova
    print("Passaggio" + str(passaggi+1) + ": ",input_text)
    nuova=""
    if passaggi==n_passaggi1-1:
        risultato_40=input_text
    passaggi+=1
#print(start)
print ("Lunghezza numero con 40 passaggi: ",len(risultato_40))
print ("Lunghezza numero con 50 passaggi: ",len(input_text))