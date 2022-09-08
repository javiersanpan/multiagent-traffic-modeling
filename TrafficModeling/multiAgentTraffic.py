import agentpy as ap
# Custom made classes and functions
from TrafficModeling.roundabout import Roundabout
from TrafficModeling.road import Road

class MultiAgentTraffic(ap.Model):
    def setup(self):
        # Read custom parameters
        self.roads_positions = self.p.roads_positions
        self.road_background = self.p.road_background
        self.cars_amount = self.p.cars_amount
        self.begin_points = self.p.begin_points

        # Create grid
        self.city = ap.Grid(self, [self.p.size] * 2, track_empty=True)

        # Create car agents
        self.cars=ap.AgentList(self,self.cars_amount)

        # Add car agents
        self.city.add_agents(self.cars, [self.begin_points[0],self.begin_points[1]])

        # Create and add road agents
        road_agents = []
        for i in range(self.cars_amount):
            road_agents.append(ap.AgentList(self, len(self.roads_positions[i])))
            self.city.add_agents(road_agents[i], positions=self.roads_positions[i] ,empty=False)

        background_road_agent = ap.AgentList(self,len(self.road_background))
        self.city.add_agents(background_road_agent, positions=self.road_background, empty=False)

        # Agent type attribute
        
        #0: untravelled road
        #1: travelled road
        #2: car 0
        #3: car 1
        road_agents[0].type_agent = 0
        road_agents[1].type_agent = 0
        background_road_agent.type_agent = 0
        
        self.cars[0].type_agent = 2
        self.cars[1].type_agent = 3

        # Road direction attribute
        #0: is vertical
        #1: is horizontal
        road_agents[0].road_direction = 0
        road_agents[1].road_direction = 1
        background_road_agent.road_direction = 2

    def step(self):
        cars = self.cars
        
        for car in cars:
            for neighbor in self.city.neighbors(car):
                new_position = self.city.positions[neighbor]
                
                if neighbor.type_agent == 0 and neighbor.road_direction == 0 and car.type_agent == 3:
                    self.city.move_to(car, new_position)
                    neighbor.type_agent = 1
                    break
                    
                if neighbor.type_agent == 0 and neighbor.road_direction == 1 and car.type_agent == 2:
                    self.city.move_to(car, new_position)
                    neighbor.type_agent = 1
                    break