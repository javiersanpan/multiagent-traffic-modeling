from re import M
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
        self.draw_north_p = False
        self.draw_south_p = False
        self.draw_east_p = False
        self.draw_west_p = False
        
    def draw_south(self):
        POSITIONS_DB = []
        for i in range(self.vertical_center + self.ratio + 1, self.size):
            POSITIONS_DB.append((i, self.horizontal_center))
        return POSITIONS_DB

    def draw_north(self):
        POSITIONS_DT = []
        for i in range(0, self.vertical_center - self.ratio + 1):
            POSITIONS_DT.append((i, self.horizontal_center))
        return POSITIONS_DT

    def draw_east(self):
        POSITIONS_DR = []
        for i in range(self.horizontal_center + self.ratio + 1, self.size):
            POSITIONS_DR.append((self.vertical_center ,i))
        return POSITIONS_DR

    def draw_west(self):
        POSITIONS_DL = []
        for i in range(1, self.horizontal_center - self.ratio):
            POSITIONS_DL.append((self.vertical_center ,i))
        return POSITIONS_DL

    def draw_missing_points(self):
        MISSING_P = []
        if self.draw_north_p: MISSING_P.append((self.vertical_center - self.ratio , self.horizontal_center))
        if self.draw_south_p: MISSING_P.append((self.vertical_center + self.ratio , self.horizontal_center))
        if self.draw_east_p: MISSING_P.append((self.vertical_center , self.horizontal_center + self.ratio))
        if self.draw_west_p: MISSING_P.append((self.vertical_center , self.horizontal_center - self.ratio))
        return MISSING_P

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

        # If entry is south
        if self.begin_p[0] == 25 and self.begin_p[1] == 13:
            POSITIONS+=self.draw_south()
            POSITIONS+=self.rab.drawBR()
            self.draw_south_p = True
            #POSITIONS.append((13,16))

            if self.end_p[0] == 13 and self.end_p[1] == 26:
                # If exit is east
                POSITIONS+=self.draw_east()
                self.draw_east_p = True

            elif self.end_p[0] == 0 and self.end_p[1] == 13:
                # If exit is north
                POSITIONS+=self.draw_north()
                POSITIONS += self.rab.drawTR()
                self.draw_north_p = True
                self.draw_east_p = True
                #POSITIONS.append((10,13))
            
            elif self.end_p[0] == 13 and self.end_p[1] == 0:
                # If exit is west
                POSITIONS+=self.draw_west()
                POSITIONS += self.rab.drawTR() + self.rab.drawTL()
                self.draw_west_p = True
                self.draw_north_p = True
                self.draw_east_p = True
                #POSITIONS.append((10,13))
                #POSITIONS.append((13,10))
            
        # If entry is east
        elif self.begin_p[0] == 13 and self.begin_p[1] == 25:
            POSITIONS+=self.draw_east()
            POSITIONS+=self.rab.drawTR()
            self.draw_east_p = True
            #POSITIONS.append((10,13))

            if self.end_p[0] == 0 and self.end_p[1] == 13:
                # If exit is north
                self.draw_north_p = True
                POSITIONS+=self.draw_north()

            elif self.end_p[0] == 13 and self.end_p[1] == 0:
                # If exit is west
                POSITIONS+=self.draw_west()
                POSITIONS+=self.rab.drawTL()
                self.draw_north_p = True
                self.draw_west_p = True

                #POSITIONS.append((13,10))

            elif self.end_p[0] == 26 and self.end_p[1] == 13:
                # If exit is south
                POSITIONS+=self.draw_south()
                POSITIONS+=self.rab.drawTL() + self.rab.drawBL()
                self.draw_north_p = True
                self.draw_west_p = True
                self.draw_south_p = True
                #POSITIONS.append((13,10))
                #POSITIONS.append((16,13))

        # If entry is north
        elif self.begin_p[0] == 1 and self.begin_p[1] == 13:
            POSITIONS+=self.draw_north()
            POSITIONS+=self.rab.drawTL()
            self.draw_west_p = True
            #POSITIONS.append((13,10))
            self.draw_north_p = True


            if self.end_p[0] == 13 and self.end_p[1] == 0:
                # If exit is west
                POSITIONS+=self.draw_west()
            
            elif self.end_p[0] == 26 and self.end_p[1] == 13:
                # If exit is south
                POSITIONS+=self.draw_south()
                POSITIONS+=self.rab.drawBL()
                self.draw_south_p = True
                #POSITIONS.append((16,13))

            elif self.end_p[0] == 13 and self.end_p[1] == 26:
                # If exit is east
                POSITIONS+=self.draw_east()
                POSITIONS+=self.rab.drawBL() + self.rab.drawBR()
                self.draw_south_p = True
                self.draw_east_p = True
                #POSITIONS.append((16,13))
                #POSITIONS.append((13,16))
        
        # If entry is west
        elif self.begin_p[0] == 13 and self.begin_p[1] == 1:
            POSITIONS+=self.draw_west()
            POSITIONS+=self.rab.drawBL()
            self.draw_west_p = True
            self.draw_south_p = True
            #POSITIONS.append((16,13))

            if self.end_p[0] == 26 and self.end_p[1] == 13:
                # If exit is south
                POSITIONS+=self.draw_south()

            elif self.end_p[0] == 13 and self.end_p[1] == 26:
                # If exit is east
                POSITIONS+=self.draw_east()
                POSITIONS+=self.rab.drawBR()
                #POSITIONS.append((13,16))
                self.draw_east_p = True


            elif self.end_p[0] == 0 and self.end_p[1] == 13:
                # If exit is north
                POSITIONS+=self.draw_north()
                POSITIONS+=self.rab.drawBR()+self.rab.drawTR()
                self.draw_east_p = True
                self.draw_north_p = True
                #POSITIONS.append((13,16))
                #POSITIONS.append((0,13))

        POSITIONS+=self.draw_missing_points()

        return POSITIONS