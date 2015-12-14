#ESERCIZIO GIORNO 1 risultato corretto 74 6595
istruzioni=open("input_es1.txt",'rb')

piano = 0
posizione=0
pos_piano=0
#for s in istruzioni:
with open("input_es1.txt",'r') as fp:
    for line in fp:
        for s in line:
            posizione+=1
            if s=="(":
                piano+=1
            else:
                piano-=1
            if piano==-1:
                pos_piano=posizione
print("Alla fine Santa Klaus si trova al piano n°: ",piano)
print("Era al piano -1 alla posizione: ",pos_piano)