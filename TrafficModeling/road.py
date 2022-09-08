from TrafficModeling.roundabout import Roundabout

class Road:
    def __init__(self, ratio, x_center, y_center, begin_p, end_p):
        # llamar a la clase roundabout y mandarle el radio para que dibuje la calle
        #self.car = car
        self.ratio = ratio
        self.x_center = x_center
        self.y_center = y_center
        self.begin_p = begin_p
        self.end_p = end_p
        self.rab = Roundabout(ratio, x_center, y_center)
  
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
        POSITIONS_BG += self.drawbottom()
        POSITIONS_BG += self.drawleft()
        POSITIONS_BG += self.drawright()
        POSITIONS_BG += self.drawtop()
        POSITIONS_BG += self.rab.drawBL() + self.rab.drawBR() + self.rab.drawTL() + self.rab.drawTR()
        return POSITIONS_BG

    def drawRoad(self):
        POSITIONS = []

        #SI SALE DE ABAJO
        if self.begin_p[0] == 26 and self.begin_p[1] == 13:
            POSITIONS+=self.drawbottom()
            POSITIONS+=self.rab.drawBR()
            POSITIONS.append((13,16))

            if self.end_p[0] == 13 and self.end_p[1] == 26:
                POSITIONS+=self.drawright()

            elif self.end_p[0] == 0 and self.end_p[1] == 13:
                POSITIONS+=self.drawtop()
                POSITIONS += self.rab.drawTR()
                POSITIONS.append((10,13))
            
            elif self.end_p[0] == 13 and self.end_p[1] == 0:
                POSITIONS+=self.drawleft()
                POSITIONS += self.rab.drawTR() + self.rab.drawTL()
                POSITIONS.append((10,13))
                POSITIONS.append((13,10))
            
        #SI SALE DE LA DERECHA
        elif self.begin_p[0] == 13 and self.begin_p[1] == 26:
            POSITIONS+=self.drawright()
            POSITIONS+=self.rab.drawTR()
            POSITIONS.append((10,13))

            if self.end_p[0] == 0 and self.end_p[1] == 13:
                POSITIONS+=self.drawtop()

            elif self.end_p[0] == 13 and self.end_p[1] == 0:
                POSITIONS+=self.drawleft()
                POSITIONS+=self.rab.drawTL()
                POSITIONS.append((13,10))

            elif self.end_p[0] == 26 and self.end_p[1] == 13:
                POSITIONS+=self.drawbottom()
                POSITIONS+=self.rab.drawTL() + self.rab.drawBL()
                POSITIONS.append((13,10))
                POSITIONS.append((16,13))

        #SI SALE DE ARRIBA
        elif self.begin_p[0] == 0 and self.begin_p[1] == 13:
            POSITIONS+=self.drawtop()
            POSITIONS+=self.rab.drawTL()
            POSITIONS.append((13,10))

            if self.end_p[0] == 13 and self.end_p[1] == 0:
                POSITIONS+=self.drawleft()
            
            elif self.end_p[0] == 26 and self.end_p[1] == 13:
                POSITIONS+=self.drawbottom()
                POSITIONS+=self.rab.drawBL()
                POSITIONS.append((16,13))

            elif self.end_p[0] == 13 and self.end_p[1] == 26:
                POSITIONS+=self.drawright()
                POSITIONS+=self.rab.drawBL() + self.rab.drawBR()
                POSITIONS.append((16,13))
                POSITIONS.append((13,16))
        
        #SI SALE DE IZQ
        elif self.begin_p[0] == 13 and self.begin_p[1] == 0:
            POSITIONS+=self.drawleft()
            POSITIONS+=self.rab.drawBL()
            POSITIONS.append((16,13))

            if self.end_p[0] == 26 and self.end_p[1] == 13:
                POSITIONS+=self.drawbottom()

            elif self.end_p[0] == 13 and self.end_p[1] == 26:
                POSITIONS+=self.drawright()
                POSITIONS+=self.rab.drawBR()
                POSITIONS.append((13,16))

            elif self.end_p[0] == 0 and self.end_p[1] == 13:
                POSITIONS+=self.drawtop()
                POSITIONS+=self.rab.drawBR()+self.rab.drawTR()
                POSITIONS.append((13,16))
                POSITIONS.append((0,13))
    
        return POSITIONS