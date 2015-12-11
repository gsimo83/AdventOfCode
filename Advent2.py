# ESERCIZIO GIORNO 2
f_input=open("Input_es2.txt",'r')

def CalcolaCarta(x,y,z):
    carta=0
    area1=(x*y)
    #print(area1)
    area2=(y*z)
    #print(area2)
    area3=(x*z)
    #print(area3)
    areaminore=0
    if area1<=area2 and area1<=area3:
        areaminore=area1
    elif area2<=area1 and area2<=area3:
        areaminore=area2
    else:
        areaminore=area3
    #carta= carta 
    #print(areaminore)
    carta=(2*area1)+(2*area2)+(2*area3)+areaminore
    return carta

def CalcolaRibbon(x,y,z):
    ribbon=0
    small1,small2,_=sorted([x,y,z])
    ribbon=2*small1 + 2*small2 + (x * y * z)
    print(ribbon)

    return ribbon

Tot=0
Tot_Ribbon=0
ListaRegali=f_input.readlines()
x=0
y=0
z=0
for riga in ListaRegali:
    x=int(riga.split('x')[0])
    y=int(riga.split('x')[1])
    z=int(riga.split('x')[2])
    Tot+=CalcolaCarta(x,y,z)
    Tot_Ribbon+=CalcolaRibbon(x,y,z)
    print("parziale Carta:", Tot)

print("Totale Carta", Tot)
print("Totale Nastro", Tot_Ribbon)

#print(sorted([ListaRegali[0], ListaRegali[1], ListaRegali[2]]))
#for terzina in ListaRegali:
#    Tot+=CalcolaCarta(terzina[0],terzina[1],terzina[2])
#    print("parziale Carta:", Tot)
#Tot_Ribbon=0
#for terzina in ListaRegali:
#    Tot_Ribbon+=CalcolaRibbon(terzina[0],terzina[1],terzina[2])
#    print("parziale ribbon:", Tot_Ribbon)