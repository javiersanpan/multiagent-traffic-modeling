import agentpy as ap
import matplotlib.pyplot as plt
import IPython

i = 0

print(i)
i += 1

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
      
print(i)
i += 1

class Road:
  def __init__(self, car, ratio, x_center, y_center, bp, ep):
    # x-5 de un lado y x+5 del otro lado
    # llamar a la clase roundabout y mandarle el radio para que dibuje la calle
      self.car = car
      self.ratio = ratio
      self.x_center = x_center
      self.y_center = y_center
      self.bp = bp
      self.ep = ep
  
  def drawRD(self):
      POSITIONS = []
      rab = Roundabout(self.ratio, self.x_center,self.y_center) #falta acceder a las partes de la rotonda

      for i in range(self.bp, 11):
        POSITIONS.append((13,i))
    
      for i in range(16, 27):
        POSITIONS_X.append((13,i))
        POSITIONS_Y.append((i,13))



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
    
  
print(i)
i += 1

# Road agent positions
POSITIONS_X = []
POSITIONS_Y = []
POSITIONS_BG = []

rab = Roundabout(3, 13, 13)

for i in range(0, 11):
    POSITIONS_X.append((13,i))
    POSITIONS_Y.append((i,13))
    
for i in range(16, 27):
    POSITIONS_X.append((13,i))
    POSITIONS_Y.append((i,13))

#POSITIONS_X = POSITIONS_X + rab.drawTL() + rab.drawTR()
#POSITIONS_X.append((10,13))

#POSITIONS_Y = POSITIONS_Y + rab.drawBR() + rab.drawTR()
#POSITIONS_Y.append((13,16))

POSITIONS_BG = rab.drawBL() + rab.drawBR()

print(i)
i += 1

class multiAgentTraffic(ap.Model):
    def setup(self):
        
        # Create agents
        self.cars=ap.AgentList(self,2)
        roadX=ap.AgentList(self,len(POSITIONS_X))
        roadY=ap.AgentList(self,len(POSITIONS_Y))
        roadBG=ap.AgentList(self,len(POSITIONS_BG))

        # Create grid
        self.city = ap.Grid(self, [self.p.size] * 2, track_empty=True)
        
        self.city.add_agents(self.cars, [(26,13),(13,26)])
        self.city.add_agents(roadX, positions=POSITIONS_X ,empty=False)
        self.city.add_agents(roadY, positions=POSITIONS_Y, empty=False)
        self.city.add_agents(roadBG, positions=POSITIONS_BG, empty=False)

        # Agent type attribute
        

        #0: untravelled road
        #1: travelled road
        #2: car 0
        #3: car 1
        
        roadX.type_agent = 0
        roadY.type_agent = 0
        roadBG.type_agent = 0
        
        self.cars[0].type_agent = 2
        self.cars[1].type_agent = 3

        # Road direction attribute
        #0: is vertical
        #1: is horizontal
        roadX.road_direction = 0
        roadY.road_direction = 1
        roadBG.road_direction = 2

    def step(self):
        cars = self.cars
        
        for car in cars:
            for neighbor in self.city.neighbors(car):
                new_position = self.city.positions[neighbor]
                
                if neighbor.type_agent == 0 and neighbor.road_direction == 0 and car.type_agent == 3:
                    #q carro e
                    #por q road se va
                    self.city.move_to(car, new_position)
                    neighbor.type_agent = 1
                    break
                    
                if neighbor.type_agent == 0 and neighbor.road_direction == 1 and car.type_agent == 2:
                    #q carro es
                    #por q road se va
                    self.city.move_to(car, new_position)
                    neighbor.type_agent = 1
                    break

print(i)
i += 1

# Define parameters
parameters={
    'size':27,
    'steps':50,
}
# Create single-run animation with custom colors
def animation_plot (model, ax):
    attr_grid=model.city.attr_grid('type_agent')
    color_dict = {0:'#808080', 1:'#ADFFBF', 2: '#FF00FF',3:'#0000FF', None: '#497a41'}
    ap.gridplot (attr_grid, ax=ax, color_dict=color_dict, convert=True)
    ax.set_title(f"Traffic simulation\n"
    f"Time-step: {model.t}")
fig, ax = plt. subplots()

model = multiAgentTraffic(parameters)

animation = ap.animate(model, fig, ax, animation_plot)

animation.save("cool.gif")
IPython.display.HTML(animation.to_jshtml(fps=15))

print(i)
i += 1
