class Point:
  def __init__(self, x, y):
    self.x, self.y = x, y
  def move_north(self, val):
    self.y += val
  def move_south(self, val):
    self.y -= val
  def move_east (self, val):
    self.x += val
  def move_west (self, val):
    self.x -=val
  def getCor(self):
    return (str(self.x) + ' ' + str(self.y))

punto_finale = Point(0,0);
distanza = 0;
with open("input2_es1.txt") as f:
    #print(punto_d.__sub__(punto_iniziale))
    for riga in f:
        riga =riga.replace(r' ',r'')
        print(riga)
        orientamento = "N"
        #direzione = if (riga[0,1] == 'L': "W" else : "E")
        for cmd in riga.split(','):
          print("mossa : " + cmd)
          print("orientamento: " + orientamento)
          mossa = cmd[0:1]
          valore =  int(cmd[1:])
          if (orientamento == 'N'):
            if (mossa == 'L') :
                # mouovi a ovest e orientamento ovest
                punto_finale.move_west(valore)
                orientamento = "W"
            else :
                # mouvi a est e orientamento a est
                punto_finale.move_east(valore)
                orientamento = "E"
          elif(orientamento== 'S'):
            if (mossa == 'L') :
                # mouovi a est e orientamento est
                punto_finale.move_east(valore)
                orientamento = "E"
            else :
                # mouvi a ovest e orientamento a ovest
                punto_finale.move_west(valore)
                orientamento = "W"
          elif(orientamento== 'E'):
            if (mossa == 'L') :
                # mouvi a nord e orientamento a nord
                punto_finale.move_north(valore)
                orientamento = "N"
            else :
                # mouvi a sud e orientamento a sud
                punto_finale.move_south(valore)
                orientamento = "S"
          else : # orientamento == W
            if (mossa == 'L') :
                # mouvi a sud e orientamento a sud
                punto_finale.move_south(valore)
                orientamento = "S"
            else :
                # mouvi a nord e orientamento a nord
                punto_finale.move_north(valore)
                orientamento = "N"
          mossa_precedente = mossa
          print("Punto arrivo : " + punto_finale.getCor())
distanza = -1 * ((punto_finale.x * -1) + (punto_finale.y * -1) )
print ("DISTANZA : " + str(distanza))