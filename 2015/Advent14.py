#costruisco una classe Renna 
class Reindeer:
    tot_distance=0
    distanze={}
    points=0
    
    def __init__(self,speed=0,time_run=0,time_to_breath=0,nome=""):
        self.speed=speed
        self.time_run=time_run
        self.time_to_breath=time_to_breath
        self.nome=nome
        self.distanze={}
        self.points=0
        
    def run(self,time=0):
        runtime=0
        i=1
        while i<=time+1:
            if runtime<self.time_run:
                self.tot_distance+=self.speed
                #print("secondo : ",str(i)," Distanza ",self.tot_distance)
                #self.distanze[i]=self.speed + self.distanze.setdefault(i-1,self.speed)
                
                runtime+=1
            else:
                i+=self.time_to_breath-1
                runtime=0
            i+=1
            
    def run_to_point(self,time=0):
        runtime=0
        pausa=0
        i=0
        print(time)
        while i<time:
            if runtime<self.time_run:
                if i==0 :
                    self.distanze[i]=self.speed
                    print(i,str(self.distanze[i]) + " --- " + str(runtime) + " --- " + str(pausa))
                else:
                    self.distanze[i]=self.distanze[i-1] + self.speed
                    print(i,str(self.distanze[i]) + " --- " + str(runtime) + " --- " + str(pausa))
                runtime+=1
                i+=1
            else:
                while pausa<self.time_to_breath and i<time:
                    self.distanze[i]=self.distanze[i-1]
                    print(i,str(self.distanze[i]) + " --- " + str(runtime) + " --- " + str(pausa))
                    pausa+=1
                    i+=1
                runtime=0
                pausa=0
        print(time)
    def get_name(self):
        return self.nome

race_time=2503
Reinners=[]
with open("input_es14.txt") as f:
    for riga in f.readlines():
        prop=riga.split(" ")
        prop[0] = Reindeer(int(prop[3]),int(prop[6]),int(prop[13]),prop[0])
        Reinners.append(prop[0])
        
n=input("Quale parte dell'esercizio vuoi risolvere (A,B) ? : ")
if(n.upper()=="A"):
    # Advent14 - Caso 1
    for renna in Reinners:
        renna.run(race_time)
        print(renna.get_name())
        print("--------------------------------------------------")
        print("Speed : ",str(renna.speed) + "km/s")
        print("Duration of single run : ", str(renna.time_run))
        print("Time to restore breath : ", str(renna.time_to_breath))
        print("Distance after " + str(race_time) + " sec. : ",renna.tot_distance)
        #print("Riepilogo:" + str(renna.distanze))
        print("--------------------------------------------------")
elif(n.upper()=="B"):
     # Advent14 - Caso 2
    for renna in Reinners:
        renna.run_to_point(race_time)
        print(renna.get_name())
        print("--------------------------------------------------")
        print("Speed : ",str(renna.speed) + "km/s")
        print("Duration of single run : ", str(renna.time_run))
        print("Time to restore breath : ", str(renna.time_to_breath))
        #print("Riepilogo:" + str(renna.distanze))


    for z in range(1,race_time+1,1):
        massimo=0
        # trovo il massimo per quel secondo
        for renna in Reinners:
            if renna.distanze[z-1]>massimo:
                massimo=renna.distanze[z-1]
            #print(renna.get_name() + " sec: " + str(z)," Distanza:" + str(renna.distanze[z]) + " massimo:" +str(massimo))
        # trovo la/le renna/e con il massimo e assegno il punto.
        for renna in Reinners:
            if renna.distanze[z-1]==massimo:
                renna.points+=1
            print(renna.get_name() + " sec: " + str(z)," Distanza:" + str(renna.distanze[z-1]) + " massimo:" +str(massimo) + " points:" + str(renna.points))
else:
    print("Valore inserito non corretto, caratteri validi 'A' e 'B'.")
# input text    
"""
Dancer can fly 27 km/s for 5 seconds, but then must rest for 132 seconds.
Cupid can fly 22 km/s for 2 seconds, but then must rest for 41 seconds.
Rudolph can fly 11 km/s for 5 seconds, but then must rest for 48 seconds.
Donner can fly 28 km/s for 5 seconds, but then must rest for 134 seconds.
Dasher can fly 4 km/s for 16 seconds, but then must rest for 55 seconds.
Blitzen can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.
Prancer can fly 3 km/s for 21 seconds, but then must rest for 40 seconds.
Comet can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.
Vixen can fly 18 km/s for 5 seconds, but then must rest for 84 seconds.
"""