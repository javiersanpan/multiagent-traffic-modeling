from TrafficModeling.roundabout import Roundabout

class Road:
    def __init__(self, ratio, x_center, y_center, bp, ep):
        # x-5 de un lado y x+5 del otro lado
        # llamar a la clase roundabout y mandarle el radio para que dibuje la calle
        #self.car = car
        self.ratio = ratio
        self.x_center = x_center
        self.y_center = y_center
        self.bp = bp
        self.ep = ep
        self.rab = Roundabout(5, 13, 13)
  
    def drawbottom(self):
        POSITIONS_DB = []
        for i in range(16,27):
            POSITIONS_DB.append((i,13))
        return POSITIONS_DB

    def drawtop(self):
        POSITIONS_DT = []
        for i in range(0,11):
            POSITIONS_DT.append((i,13))
        return POSITIONS_DT

    def drawright(self):
        POSITIONS_DR = []
        for i in range(16,27):
            POSITIONS_DR.append((13,i))
        return POSITIONS_DR

    def drawleft(self):
        POSITIONS_DL = []
        for i in range(0,11):
            POSITIONS_DL.append((i,13))
        return POSITIONS_DL

#POSITIONS
    def drawBG(self):
        POSITIONS_BG = []
        #dibujar posiciones del background
        POSITIONS_BG.append(self.drawbottom())
        POSITIONS_BG.append(self.drawleft())
        POSITIONS_BG.append(self.drawright())
        POSITIONS_BG.append(self.drawtop())
        POSITIONS_BG += self.rab.drawBL() + self.rab.drawBR() + self.rab.drawTL() + self.rab.drawTR()
        return POSITIONS_BG

    def drawRD(self):
        # POSSIBLE_TARGETS = [(26,13), (13,26),  (0,13), (13,0)]
        POSITIONS = []

        #primera salida: 13, 26
        #2nda salida: 0,13
        #3era salida: 13,0

        rab = Roundabout(self.ratio, self.x_center, self.y_center) #falta acceder a las partes de la rotonda
        #checar por donde viene y qué dibuja depende del bp y ep

        #SI SALE DE ABAJO
        if self.bp[0] == 26 and self.bp[1] == 13:
            POSITIONS.append(self.drawbottom())
            POSITIONS+=rab.drawBR()
            POSITIONS.append((13,16))

            if self.ep[0] == 13 and self.ep[1] == 26:
                POSITIONS.append(self.drawright())

            elif self.ep[0] == 0 and self.ep[1] == 13:
                POSITIONS.append(self.drawtop()) 
                POSITIONS += rab.drawTR()
                POSITIONS.append((10,13))
            
            elif self.ep[0] == 13 and self.ep[1] == 0:
                POSITIONS.append(self.drawleft())
                POSITIONS += rab.drawTR() + rab.drawTL()
                POSITIONS.append((10,13))
                POSITIONS.append((13,10))
            
        #SI SALE DE LA DERECHA
        elif self.bp[0] == 13 and self.bp[1] == 26:
            POSITIONS.append(self.drawright())
            POSITIONS+=rab.drawTR()
            POSITIONS.append((10,13))

            if self.ep[0] == 0 and self.ep[1] == 13:
                POSITIONS.append(self.drawtop())

            elif self.ep[0] == 13 and self.ep[1] == 0:
                POSITIONS.append(self.drawleft())
                POSITIONS+=rab.drawTL()
                POSITIONS.append((13,10))

            elif self.ep[0] == 26 and self.ep[1] == 13:
                POSITIONS.append(self.drawbottom())
                POSITIONS+=rab.drawTL() + rab.drawBL()
                POSITIONS.append((13,10))
                POSITIONS.append((16,13))

        #SI SALE DE ARRIBA
        elif self.bp[0] == 0 and self.bp[1] == 13:
            POSITIONS.append(self.drawtop())
            POSITIONS+=rab.drawTL()
            POSITIONS.append((13,10))

            if self.ep[0] == 13 and self.ep[1] == 0:
                POSITIONS.append(self.drawleft())
            
            elif self.ep[0] == 26 and self.ep[1] == 13:
                POSITIONS.append(self.drawbottom())
                POSITIONS+=rab.drawBL()
                POSITIONS.append((16,13))

            elif self.ep[0] == 13 and self.ep[1] == 26:
                POSITIONS.append(self.drawright())
                POSITIONS+=rab.drawBL() + rab.drawBR()
                POSITIONS.append((16,13))
                POSITIONS.append((13,16))
        
        #SI SALE DE IZQ
        elif self.bp[0] == 13 and self.bp[1] == 0:
            POSITIONS.append(self.drawleft())
            POSITIONS+=rab.drawBL()
            POSITIONS.append((16,13))

            if self.ep[0] == 26 and self.ep[1] == 13:
                POSITIONS.append(self.drawbottom())

            elif self.ep[0] == 13 and self.ep[1] == 26:
                POSITIONS.append(self.drawright())
                POSITIONS+=rab.drawBR()
                POSITIONS.append((13,16))

            elif self.ep[0] == 0 and self.ep[1] == 13:
                POSITIONS.append(self.drawtop())
                POSITIONS+=rab.drawBR()+rab.drawTR()
                POSITIONS.append((13,16))
                POSITIONS.append((0,13))
    
        return POSITIONS
  