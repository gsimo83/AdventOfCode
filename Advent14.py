# Advent14 - Caso 1

#costruisco una classe Renna 
class Reindeer:
    tot_distance=0
    def __init__(self,speed=0,time_run=0,time_to_breath=0,nome=""):
        self.speed=speed
        self.time_run=time_run
        self.time_to_breath=time_to_breath
        self.nome=nome
    def run(self,time=0):
        runtime=0
        i=1
        while i<=time+1:
            if runtime<self.time_run:
                self.tot_distance+=self.speed
                #print("secondo : ",str(i)," Distanza ",self.tot_distance)
                runtime+=1
            else:
                i+=self.time_to_breath-1
                runtime=0
            i+=1
    def get_name(self):
        return self.nome

race_time=2503
Reinners=[]
with open("input_es14.txt") as f:
    for riga in f.readlines():
        prop=riga.split(" ")
        prop[0] = Reindeer(int(prop[3]),int(prop[6]),int(prop[13]),prop[0])
        Reinners.append(prop[0])

for renna in Reinners:
    renna.run(race_time)
    print(renna.get_name())
    print("--------------------------------------------------")
    print("Speed : ",str(renna.speed) + "km/s")
    print("Duration of single run : ", str(renna.time_run))
    print("Time to restore breath : ", str(renna.time_to_breath))
    print("Distance after " + str(race_time) + " sec. : ",renna.tot_distance)
    print("--------------------------------------------------")