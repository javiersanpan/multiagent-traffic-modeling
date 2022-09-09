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
        
    def draw_south(self, intersection_position="center"):
        # Possible intersection positions
        # center, entry, exit
        if intersection_position == "center":
            intersection = self.horizontal_center
        elif intersection_position == "entry":
            intersection = self.horizontal_center + 1
        elif intersection_position == "exit":
            intersection = self.horizontal_center - 1
        
        POSITIONS_DB = []
        for i in range(self.vertical_center + self.ratio + 1, self.size):
            POSITIONS_DB.append((i, intersection))
        return POSITIONS_DB

    def draw_north(self, intersection_position="center"):
        if intersection_position == "center":
            intersection = self.horizontal_center
        elif intersection_position == "entry":
            intersection = self.horizontal_center - 1
        elif intersection_position == "exit":
            intersection = self.horizontal_center + 1

        POSITIONS_DT = []
        for i in range(0, self.vertical_center - self.ratio):
            POSITIONS_DT.append((i, intersection))
        return POSITIONS_DT

    def draw_east(self, intersection_position="center"):
        if intersection_position == "center":
            intersection = self.vertical_center
        elif intersection_position == "entry":
            intersection = self.vertical_center - 1
        elif intersection_position == "exit":
            intersection = self.vertical_center + 1

        POSITIONS_DR = []
        for i in range(self.horizontal_center + self.ratio + 1, self.size):
            POSITIONS_DR.append((intersection ,i))
        return POSITIONS_DR

    def draw_west(self, intersection_position="center"):
        if intersection_position == "center":
            intersection = self.vertical_center
        elif intersection_position == "entry":
            intersection = self.vertical_center + 1
        elif intersection_position == "exit":
            intersection = self.vertical_center - 1

        POSITIONS_DL = []
        for i in range(1, self.horizontal_center - self.ratio):
            POSITIONS_DL.append((intersection ,i))
        return POSITIONS_DL

    def draw_missing_points(self, all=False):
        MISSING_P = []
        if self.draw_north_p or all: MISSING_P.append((self.vertical_center - self.ratio , self.horizontal_center))
        if self.draw_south_p or all: MISSING_P.append((self.vertical_center + self.ratio , self.horizontal_center))
        if self.draw_east_p or all: MISSING_P.append((self.vertical_center , self.horizontal_center + self.ratio))
        if self.draw_west_p or all: MISSING_P.append((self.vertical_center , self.horizontal_center - self.ratio))
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
        POSITIONS_BG += self.draw_missing_points(all=True)
        return POSITIONS_BG

    def drawRoad(self):
        POSITIONS = []
        # If entry is south
        if self.begin_p[0] == self.size - 1 and self.begin_p[1] == self.horizontal_center + 1:
            POSITIONS+=self.draw_south("entry")
            POSITIONS+=self.rab.drawBR()
            
            # If exit is east
            if self.end_p[0] == 13 and self.end_p[1] == 26:
                POSITIONS+=self.draw_east()

            # If exit is north
            elif self.end_p[0] == 0 and self.end_p[1] == self.horizontal_center + 1:
                POSITIONS += self.draw_north("exit")
                POSITIONS += self.rab.drawTR()
                self.draw_east_p = True
                POSITIONS.remove((self.vertical_center - self.ratio, self.horizontal_center + 1))

             # If exit is west
            elif self.end_p[0] == 13 and self.end_p[1] == 0:
                POSITIONS += self.draw_west()
                POSITIONS += self.rab.drawTR() + self.rab.drawTL()
                self.draw_north_p = True
                self.draw_east_p = True
            
        # If entry is east
        elif self.begin_p[0] == self.vertical_center - 1 and self.begin_p[1] == self.size - 1:
            POSITIONS+=self.draw_east("entry")
            POSITIONS+=self.rab.drawTR()

            # If exit is north
            if self.end_p[0] == 0 and self.end_p[1] == 13: 
                POSITIONS+=self.draw_north()

            # If exit is west
            elif self.end_p[0] == 13 and self.end_p[1] == 0:
                POSITIONS+=self.draw_west()
                POSITIONS+=self.rab.drawTL()
                self.draw_north_p = True

            # If exit is south
            elif self.end_p[0] == self.size - 1 and self.end_p[1] == self.horizontal_center - 1:
                POSITIONS+=self.draw_south("exit")
                POSITIONS+=self.rab.drawTL() + self.rab.drawBL()
                self.draw_north_p = True
                self.draw_west_p = True
                POSITIONS.remove((self.vertical_center + self.ratio,self.horizontal_center - 1))

        # If entry is north
        elif self.begin_p[0] == 1 and self.begin_p[1] == self.horizontal_center - 1:
            POSITIONS+=self.draw_north()
            POSITIONS+=self.rab.drawTL()

            # If exit is west
            if self.end_p[0] == 13 and self.end_p[1] == 0:
                POSITIONS+=self.draw_west()
            
            # If exit is south
            elif self.end_p[0] == 26 and self.end_p[1] == 13:
                POSITIONS+=self.draw_south()
                POSITIONS+=self.rab.drawBL()
                self.draw_west_p = True

            # If exit is east
            elif self.end_p[0] == 13 and self.end_p[1] == 26:
                POSITIONS+=self.draw_east()
                POSITIONS+=self.rab.drawBL() + self.rab.drawBR()
                self.draw_south_p = True
                self.draw_west_p = True
        
        # If entry is west
        elif self.begin_p[0] == self.vertical_center + 1 and self.begin_p[1] == 1:
            POSITIONS+=self.draw_west("entry")
            POSITIONS+=self.rab.drawBL()

            # If exit is south
            if self.end_p[0] == 26 and self.end_p[1] == 13:
                POSITIONS+=self.draw_south()

            # If exit is east
            elif self.end_p[0] == self.vertical_center + 1 and self.end_p[1] == self.size - 1:
                POSITIONS+=self.draw_east("exit")
                POSITIONS+=self.rab.drawBR()
                self.draw_south_p = True
                POSITIONS.remove((self.vertical_center + 1 ,self.horizontal_center + self. ratio))

            # If exit is north
            elif self.end_p[0] == 0 and self.end_p[1] == 13:
                POSITIONS+=self.draw_north()
                POSITIONS+=self.rab.drawBR()+self.rab.drawTR()
                self.draw_east_p = True
                self.draw_south_p = True

        POSITIONS+=self.draw_missing_points()

        return POSITIONS