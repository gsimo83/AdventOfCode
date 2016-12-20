##Esercizio 3 # con il mio input il risultato corretto deve essere 2572

#  First Solution : no so good ! I wanna assign a value for each move, imagining a big net where for each move on the y we have moving of Santa's +-10000 and on the x we have moving of Santa's +-1. When we have all the values of the moves, we have to count the single values in the array. I need a big value for y (10000) and a minimal for x to evitate that the x increase reaches an y value. 

matrice=[]
def MuoviSanta(mossa):
    global posizione
    if mossa=="<":
        posizione-=1
    elif mossa==">":
        posizione+=1
    elif mossa=="^":
        posizione+=10000
    else:
        posizione-=10000
    return posizione

#Leggo la mappa
input_file=open("input_es3.txt")
n_case_visitate=0
posizione=5550
n_case_doppie=0
n_mosse=0
matrice.append([posizione])
case_visitate=[]
for c in input_file.read():
    n_mosse+=1
    posizione=MuoviSanta(c)
    matrice.append([posizione])
    trovata=False
    for v in case_visitate:
        if posizione==v:
            trovata=True
    if trovata==False:
        n_case_visitate+=1
        case_visitate.append(posizione)
    else:
        n_case_doppie+=1
print("N° moves:",n_mosse)
print("Case 1 sol.1 - Single houses visited:",n_case_visitate)
#print("Case con almeno 2 visite:",n_case_doppie)

# I have found a better solution by looking on the help (thanks https://github.com/nvojkovic) : Using Python "set" that can not contain duplicate and the creation of a set of coordinates . ( with the first idea I had a lot of trouble finding the right range increment per move and likely increasing the moves may not always work )
with open("input_es3.txt") as f:
	x = 0
	y = 0
	houses = set([(0,0)])
	for c in f.read():
		if c == 'v':
			y -= 1
		elif c == '^':
			y += 1
		elif c == '<':
			x -= 1
		elif c == '>':
			x +=1
		houses.add((x,y))
	print("Case 1 sol.2 (better) - Single houses visited :",len(houses))
    
with open("input_es3.txt") as f:
    housesSanta= set([(0,0)])
    housesRobo= set([(0,0)])
    housesTot= set([(0,0)])
    i=0
    x=0
    y=0
    xx=0
    yy=0
    for h in f.read():
        if i%2==0:
            if h == 'v':
                yy -= 1
            elif h == '^':
                yy += 1
            elif h == '<':
                xx -= 1
            elif h == '>':
                xx +=1     
            housesRobo.add((xx,yy))
            housesTot.add((xx,yy))
        else:
            if h == 'v':
                y -= 1
            elif h == '^':
                y += 1
            elif h == '<':
                x -= 1
            elif h == '>':
                x +=1     
            housesSanta.add((x,y))
            housesTot.add((x,y))
        i+=1
    print("Case 2 - Single houses visited by Santa's:",len(housesSanta))
    print("Case 2 - Single houses visited by RoboClaus:",len(housesRobo))
    print("Case 2 (solution) - Single houses visited by Santa's and RoboClaus:",len(housesTot))  