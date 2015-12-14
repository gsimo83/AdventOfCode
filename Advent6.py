##Esercizio 6
from collections import defaultdict
luci=defaultdict(int)

on = lambda x: 1 
off = lambda x: 0
toggle = lambda x: 1-x
on2 = lambda x: x+1 # 0 
off2 = lambda x: x-1 # 1
toggle2 = lambda x: x+2 # 1-x
#
#
def AccendiSpegni(inizio,fine,evento,es):
    start_x,start_y=map(int,inizio.split(","))
    end_x,end_y=map(int,fine.split(","))
    for x in range(start_x,end_x+1):
        for y in range(start_y,end_y+1):
            if es==2:
                luci[(x,y)] = max(evento(luci[(x,y)]),0)
            else:
                luci[(x,y)] = evento(luci[(x,y)])
                
with open("input_es6.txt") as f:
    for riga in f.readlines():
        coordinate=riga.split(" ")
        if riga.startswith("turn on"):
            AccendiSpegni(coordinate[2],coordinate[4],on,1)
        elif riga.startswith("turn off"):
            AccendiSpegni(coordinate[2],coordinate[4],off,1)
        elif riga.startswith("toggle "):
            AccendiSpegni(coordinate[1],coordinate[3],toggle,1)
print(sum(luci.values()))
luci=defaultdict(int)

with open("input_es6.txt") as f:
    for riga in f.readlines():
        coordinate=riga.split(" ")
        if riga.startswith("turn on"):
            AccendiSpegni(coordinate[2],coordinate[4],on2,2)
        elif riga.startswith("turn off"):
            AccendiSpegni(coordinate[2],coordinate[4],off2,2)
        elif riga.startswith("toggle "):
            AccendiSpegni(coordinate[1],coordinate[3],toggle2,2)
print(sum(luci.values()))