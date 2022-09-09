import agentpy as ap

class MultiAgentTraffic(ap.Model):
    def setup(self):
        self.car0cords = []
        self.car1cords = []
        self.car2cords = []
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
        self.city.add_agents(self.cars, self.begin_points)

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
        #n >= 2: car n-2
        for i in range(self.cars_amount):
            road_agents[i].type_agent = 0
            self.cars[i].type_agent = i + 2
        
        background_road_agent.type_agent = 0

        # Road direction attribute
        # Each element is a road for a different car agent
        background_road_agent.road_direction = 0
        for i in range(self.cars_amount):
            road_agents[i].road_direction = i + 1

    def step(self):
        cars = self.cars
        
        for car in cars:
            for neighbor in self.city.neighbors(car):
                new_position = self.city.positions[neighbor]
                
                if neighbor.type_agent == 0 and neighbor.road_direction == 1 and car.type_agent == 2:
                    self.city.move_to(car, new_position)
                    neighbor.type_agent = 1

                    arrElem = str(new_position)[1:-1]
                    self.car0cords.append(arrElem)
                    break
                    
                if neighbor.type_agent == 0 and neighbor.road_direction == 2 and car.type_agent == 3:
                    self.city.move_to(car, new_position)
                    neighbor.type_agent = 1

                    arrElem = str(new_position)[1:-1]
                    self.car1cords.append(arrElem)
                    break

                if neighbor.type_agent == 0 and neighbor.road_direction == 3 and car.type_agent == 4:
                    self.city.move_to(car, new_position)
                    neighbor.type_agent = 1

                    arrElem = str(new_position)[1:-1]
                    self.car2cords.append(arrElem)
                    break

        jsonFile = open("output/cords.json", "w")
        jsonContent = {"car0":self.car0cords,"car1":self.car1cords,"car2":self.car2cords} 
        jsonContent = str(jsonContent).replace("\'","\"")
        jsonFile.write(str(jsonContent))
        jsonFile.close()