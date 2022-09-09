from TrafficModeling.roundabout import Roundabout

class Road:
    def __init__(self, ratio, vertical_center, horizontal_center, begin_p, end_p, size):
        self.ratio = ratio
        self.vertical_center = vertical_center
        self.horizontal_center = horizontal_center
        self.begin_p = begin_p
        self.end_p = end_p
        self.rab = Roundabout(ratio, vertical_center, horizontal_center)
        self.size = size

        # Set which missing points should be added
        draw_north_p = False
        draw_south_p = False
        draw_east_p = False
        draw_west_p = False
        
    def draw_south(self):
        POSITIONS_DB = []
        for i in range(self.vertical_center + self.ratio + 1, self.size):
            POSITIONS_DB.append((i, self.horizontal_center))
        return POSITIONS_DB

    def draw_north(self):
        POSITIONS_DT = []
        for i in range(0, self.vertical_center - self.ratio):
            POSITIONS_DT.append((i, self.horizontal_center))
        return POSITIONS_DT

    def draw_east(self):
        POSITIONS_DR = []
        for i in range(self.horizontal_center + self.ratio + 1, self.size):
            POSITIONS_DR.append((self.vertical_center ,i))
        return POSITIONS_DR

    def draw_west(self):
        POSITIONS_DL = []
        for i in range(self.horizontal_center - self.ratio):
            POSITIONS_DL.append((self.vertical_center ,i))
        return POSITIONS_DL

    def draw_missing_points(self):
        MISSING_P = []
        if self.draw_east_p:
            MISSING_P.append((13,16))

#POSITIONS
    def draw_background(self):
        POSITIONS_BG = []
        # Draw background road
        POSITIONS_BG += self.draw_south()
        POSITIONS_BG += self.draw_west()
        POSITIONS_BG += self.draw_east()
        POSITIONS_BG += self.draw_north()
        POSITIONS_BG += self.rab.drawBL() + self.rab.drawBR() + self.rab.drawTL() + self.rab.drawTR()
        return POSITIONS_BG

    def drawRoad(self):
        POSITIONS = []

        # If exit is south
        if self.begin_p[0] == 26 and self.begin_p[1] == 13:
            POSITIONS+=self.draw_south()
            POSITIONS+=self.rab.drawBR()
            #POSITIONS.append((13,16))

            if self.end_p[0] == 13 and self.end_p[1] == 26:
                POSITIONS+=self.draw_east()

            elif self.end_p[0] == 0 and self.end_p[1] == 13:
                POSITIONS+=self.draw_north()
                POSITIONS += self.rab.drawTR()
                #POSITIONS.append((10,13))
            
            elif self.end_p[0] == 13 and self.end_p[1] == 0:
                POSITIONS+=self.draw_west()
                POSITIONS += self.rab.drawTR() + self.rab.drawTL()
                #POSITIONS.append((10,13))
                #POSITIONS.append((13,10))
            
        # If exit is east
        elif self.begin_p[0] == 13 and self.begin_p[1] == 26:
            POSITIONS+=self.draw_east()
            POSITIONS+=self.rab.drawTR()
            #POSITIONS.append((10,13))

            if self.end_p[0] == 0 and self.end_p[1] == 13:
                POSITIONS+=self.draw_north()

            elif self.end_p[0] == 13 and self.end_p[1] == 0:
                POSITIONS+=self.draw_west()
                POSITIONS+=self.rab.drawTL()
                #POSITIONS.append((13,10))

            elif self.end_p[0] == 26 and self.end_p[1] == 13:
                POSITIONS+=self.draw_south()
                POSITIONS+=self.rab.drawTL() + self.rab.drawBL()
                #POSITIONS.append((13,10))
                #POSITIONS.append((16,13))

        # If exit is north
        elif self.begin_p[0] == 0 and self.begin_p[1] == 13:
            POSITIONS+=self.draw_north()
            POSITIONS+=self.rab.drawTL()
            #POSITIONS.append((13,10))

            if self.end_p[0] == 13 and self.end_p[1] == 0:
                POSITIONS+=self.draw_west()
            
            elif self.end_p[0] == 26 and self.end_p[1] == 13:
                POSITIONS+=self.draw_south()
                POSITIONS+=self.rab.drawBL()
                #POSITIONS.append((16,13))

            elif self.end_p[0] == 13 and self.end_p[1] == 26:
                POSITIONS+=self.draw_east()
                POSITIONS+=self.rab.drawBL() + self.rab.drawBR()
                #POSITIONS.append((16,13))
                #POSITIONS.append((13,16))
        
        # If exit is west
        elif self.begin_p[0] == 13 and self.begin_p[1] == 0:
            POSITIONS+=self.draw_west()
            POSITIONS+=self.rab.drawBL()
            #POSITIONS.append((16,13))

            if self.end_p[0] == 26 and self.end_p[1] == 13:
                POSITIONS+=self.draw_south()

            elif self.end_p[0] == 13 and self.end_p[1] == 26:
                POSITIONS+=self.draw_east()
                POSITIONS+=self.rab.drawBR()
                #POSITIONS.append((13,16))

            elif self.end_p[0] == 0 and self.end_p[1] == 13:
                POSITIONS+=self.draw_north()
                POSITIONS+=self.rab.drawBR()+self.rab.drawTR()
                #POSITIONS.append((13,16))
                #POSITIONS.append((0,13))
    
        return POSITIONS