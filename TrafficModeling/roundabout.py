class Roundabout:
    def __init__(self, ratio, x_center, y_center):
        self.ratio = ratio
        self.x_center = x_center
        self.y_center = y_center
     
    def drawTR(self):
        x = self.ratio
        y = 0
        P = 1 - self.ratio
        
        cords = []
        while x > y:
            y += 1
            if P <= 0:
                P = P + 2 * y + 1
            else:        
                x -= 1
                P = P + 2 * y - 2 * x + 1
            if (x < y):
                break
        
            cords.append((-x + self.x_center, y + self.y_center))
            
            if x != y:
                cords.append((-y + self.x_center, x + self.y_center))
                
        return cords
  
    def drawBR(self):
        x = self.ratio
        y = 0
        P = 1 - self.ratio
        
        cords = []
        while x > y:
            y += 1
            if P <= 0:
                P = P + 2 * y + 1
            else:        
                x -= 1
                P = P + 2 * y - 2 * x + 1
            if (x < y):
                break
        
            cords.append((x + self.x_center, y + self.y_center))
            
            if x != y:
                cords.append((y + self.x_center, x + self.y_center))
                
        return cords
    
    def drawBL(self):
        x = self.ratio
        y = 0
        P = 1 - self.ratio
        
        cords = []
        while x > y:
            y += 1
            if P <= 0:
                P = P + 2 * y + 1
            else:        
                x -= 1
                P = P + 2 * y - 2 * x + 1
            if (x < y):
                break
        
            cords.append((x + self.x_center, -y + self.y_center))
            
            if x != y:
                cords.append((y + self.x_center, -x + self.y_center))
                
        return cords

    def drawTL(self):
        x = self.ratio
        y = 0
        P = 1 - self.ratio
        
        cords = []
        while x > y:
            y += 1
            if P <= 0:
                P = P + 2 * y + 1
            else:        
                x -= 1
                P = P + 2 * y - 2 * x + 1
            if (x < y):
                break
        
            cords.append((-x + self.x_center, -y + self.y_center))
            
            if x != y:
                cords.append((-y + self.x_center, -x + self.y_center))
        return cords
                