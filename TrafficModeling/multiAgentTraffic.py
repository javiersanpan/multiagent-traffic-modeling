import agentpy as ap
# Custom made classes and functions
from TrafficModeling.roundabout import Roundabout
from TrafficModeling.road import Road

class MultiAgentTraffic(ap.Model):
    def setup(self):
        #self.cars = ap.AgentList(self,2)
        #self.roadBG = ap.AgentList(self,len(road.drawBG()))

        # Read custom parameters
        self.roads_positions = self.p.roads_positions
        self.road_background = self.p.road_background
        self.cars_amount = self.p.cars_amount

        #QUITAR
        self.POSITIONS_X = self.p.POSITIONS_X
        self.POSITIONS_Y = self.p.POSITIONS_Y
        self.POSITIONS_BG = self.p.POSITIONS_BG
        
        # Create agents
        self.cars=ap.AgentList(self,2)
        roadX=ap.AgentList(self,len(self.POSITIONS_X))
        roadY=ap.AgentList(self,len(self.POSITIONS_Y))
        roadBG=ap.AgentList(self,len(self.POSITIONS_BG))

        # Create grid
        self.city = ap.Grid(self, [self.p.size] * 2, track_empty=True)
        
        self.city.add_agents(self.cars, [(26,13),(13,26)])
        self.city.add_agents(roadX, positions=self.POSITIONS_X ,empty=False)
        self.city.add_agents(roadY, positions=self.POSITIONS_Y, empty=False)
        self.city.add_agents(roadBG, positions=self.POSITIONS_BG, empty=False)

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